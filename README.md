# messenger-emulator
Messenger Emulator (for Ren'Py).
 
Already contains an example of dialogue.

![screenshot](https://pp.userapi.com/c849528/v849528789/c7282/fZSuh5rjNAI.jpg)

# Features
  - Sending a Text Message;
  - Sending a Picture Message (Click open to full screen);
  - Sending an Audio Message (Audio Player);
  - Typewriter Mode (typing emulation);
  - Make Choices (inside a bubble with a message);
  - Message Search (Magnifier Icon);
  - In Search '#pic' - show all Picture Messages;
  - In Search '#audio' - show all Audio Messages.

The project uses the Python module '[mutagen](https://pypi.org/project/mutagen/)'

# Installation
Add files to folder ```your_renpy_project/game```

 # Init
```
message_time = True # if True - get current time / or [hours, minutes] / or False
in_history = True # add messages to history
choice_number = True # default 1. choice1 / 2. choice2 / etc. / or False
click_to_continue = False # if False - live mode messages
time_to_send_pm = 2.0 # time to send picture message
time_to_send_am = 2.0 # time to send audio message
under_messenger = True # set False if you don't need a darker background under messenger

typewriter = True # if False - you instantly send a message
typewriter_speed = 2 # how fast you type

interlocutor = "user_name" # interlocutor's name
interlocutor_online = True # interlocutor status
interlocutor_typing = True # if False - interlocutor instantly sends a message
interlocutor_extra_time = 2.0 # extra writing time
interlocutor_typing_speed = 0.05 # default speed 0.05 * number of letters
```

# Usage
```
# Functions:
msg ("text") # Send a message
show_messenger() # show screen messenger
hide_messenger() # hide screen messenger
del_last_msg() # delete the last message
del_previous_msg() # delete all messages except last
del_all_msg() # delete all messages
find('text') # return a list of messages with 'text'

# Function Arguments 'msg':
who = 0 # if 0 - you, if 1 - interlocutor
audio = 'audio_name' # sends an audio message
pic = 'pic_name' # sends a picture
choices = { id:{'jump':'label_name', 'name':'text'}, id:{'jump':'label_name', 'name':'text'} }
status = 'online' / 'offline' # interlocutor status 

# Examples
msg ("Hi.") # Text Message from you
msg ("What's up", who=1) # Text Message from interlocutor
msg (None, pic='raven') # Picutre Message
msg (None, audio='opening', who=1) # Audio Message
msg (None, choices={0:{'jump':'park', 'name':"Go to the park"}, 1:{'jump':'movie', 'name':"Go to the movies"}})

```

# License
[MIT](https://github.com/sDextra/messenger-emulator/blob/master/LICENSE/).
