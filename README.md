# Messenger Emulator (Ren'Py)
Already contains an example of dialogue.

![screenshot](https://pp.userapi.com/c849528/v849528789/c7282/fZSuh5rjNAI.jpg)
![screenshot](https://sun9-45.userapi.com/c855324/v855324784/f620d/0VIvpiVzSCI.jpg)

## Features
  - Group Chat
  - Dialogue Switch System
  - Sending a Text Message;
  - Sending a Picture Message (Click open to full screen);
  - Sending an Audio Message (Audio Player);
  - Typewriter Mode (typing emulation);
  - Make Choices (inside the message bubble);
  - Message Search (Magnifier Icon);
  - In Search '#pic' - show all Picture Messages;
  - In Search '#audio' - show all Audio Messages.
  - Name Input Function
  - Custom Color Themes

The project uses the Python module '[mutagen](https://pypi.org/project/mutagen/)'

## Installation
Add files to folder ```your_renpy_project/game```

If you already have GUI, no need to replace it.

## Init
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

groupchat_enable = True # group chat is on
groupchat = GroupChat(name='Chat') # group chat Name
active_groupchat = groupchat # set active group chat
dialogue_one = [] # creating a new dialogue, any number of dialogs can be created
```

## Usage
```
# Functions
msg ("text") # send a message
show_messenger() # show screen messenger
hide_messenger() # hide screen messenger
del_last_msg() # delete the last message
del_previous_msg() # delete all messages except last
del_all_msg() # delete all messages
find('text') # return a list of messages with 'text'
switch_dialogue(name='AnyName', dialogue=dialogue_list) # switching active dialogue

# Function Arguments 'msg'
who = 0 # 0 - you / 1, 2, ..., etc.  your interlocutor
pic = 'pic_name' # sends a picture
audio = 'audio_name' # sends an audio message
choices = { id:{'jump':'lb1', 'name':'text1'}, id:{'jump':'lb2', 'name':'text2'} } # make a choice
status = 'online' / 'offline' # interlocutor status 
name_input = True # enter your name in the text message

# Examples
switch_dialogue(name='sDextra', dialogue=dialogue_one)
msg ("Hi.") # text message from you
msg ("What's up", who=1) # text message from the interlocutor
msg (None, pic='raven') # picture message
msg (None, audio='opening', who=1) # audio message
msg (None, choices={0:{'jump':'park', 'name':"Go to the park"}, 1:{'jump':'movie', 'name':"Go to the movies"}})
msg (None, name_input=True) # enter your name
```

## License
[MIT](https://github.com/sDextra/messenger-emulator/blob/master/LICENSE/).
