# messenger-emulator
Messenger Emulator (for Ren'Py).
 
Already contains an example of dialogue.

![screenshot](https://pp.userapi.com/c849528/v849528789/c7282/fZSuh5rjNAI.jpg)

# Features
  1. Sending a Text Message;
  2. Sending a Picture Message (Click open to full screen);
  3. Sending a Audio Message (Audio Player);
  4. Typewriter Mode (typing emulation);
  5. Message Search (Magnifier Icon);
  6. In Search '#pic' - show all Picture Messages;
  7. In Search '#audio' - show all Audio Messages.

The project uses the Python module'[mutagen](https://pypi.org/project/mutagen/)'


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

# Installation
Add files to folder ```your_renpy_project/game```

# License
[MIT](https://github.com/sDextra/messenger-emulator/blob/master/LICENSE/).
