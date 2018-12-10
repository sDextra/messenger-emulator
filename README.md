# messenger-emulator
Messenger Emulator (Ren'Py)

# Features
  1. Sending a Text Message
  2. Sending a Picture Message (Click open to full screen)
  3. Sending a Sound Message (Sound Player)
  4. Typewriter Mode (typing emulation)
  5. Message Search (Magnifier Icon)
  6. In Search '#pic' - show all Picture Messages
  7. In Search '#sound' - show all Sound Messages
  
 # Init
```
    message_time = [9,40] # [hours, minutes] # if you don't need time, you can set False
    in_history = True # add messages to history
    choice_number = True # default 1. choice1 / 2. choice2 / etc., you can set False
    click_to_continue = False # if False - live mode messages

    typewriter = True # if False - you instantly send a message
    typewriter_speed = 2 # how fast you type

    interlocutor = "user_name" # interlocutor's name
    interlocutor_online = True # interlocutor status
    interlocutor_typing = True # if False - interlocutor instantly sends a message
    interlocutor_typing_speed = 0.05 # default speed 0.05 * number of letters

```

# License
[MIT](https://github.com/sDextra/messenger-emulator/blob/master/LICENSE/).
