#################################################################################
# by sDextra 
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################

#################################################################################
# Tooltip
#################################################################################
screen tooltip(n=1, time=4.0):
    zorder 10
    $ dic = {  1:'Try typing anything. When you`re done press Space/Enter/LMB.',
               2:'You can click on the picture or player',
            }
    frame maximum 800,200 at move_tooltip xpadding 40 ypadding 30:
        text dic.get(n) align .5,.45
    $ screen_name = renpy.current_screen().screen_name
    timer time action Hide(screen_name)

init python:
    def show_tooltip(n=1):
        renpy.hide_screen('tooltip')
        renpy.show_screen('tooltip', n=n)
#################################################################################

#################################################################################
init:
    $ name = u'not sDextra' # default your name
define nm = DynamicCharacter("name") # your character
#################################################################################

#################################################################################
label start:
    $ unfreeze()

    $ messages = [] # list of all messages

    $ message_time = True # if True - get current time / or [hours, minutes] / or False
    $ in_history = True # add messages to history
    $ choice_number = True # default 1. choice1 / 2. choice2 / etc. / or False
    $ click_to_continue = False # if False - live mode messages
    $ time_to_send_pm = 2.0 # time to send picture message
    $ time_to_send_am = 2.0 # time to send audio message
    $ under_messenger = True # set False if you don't need a darker background under messenger

    $ typewriter = True # if False - you instantly send a message
    $ typewriter_speed = 2 # how fast you type

    $ interlocutor = "sDextra" # interlocutor's name
    $ interlocutor_online = True # interlocutor status
    $ interlocutor_typing = True # if False - interlocutor instantly sends a message
    $ interlocutor_extra_time = 2.0 # extra writing time
    $ interlocutor_typing_speed = 0.05 # default speed 0.1 * number of letters

    $ name = renpy.input(u"Who Am I?", length=25).title() # your name

label dialogue:
    "*This dialogue is an example of the work of the {a=https://github.com/sDextra/messenger-emulator}\"Messenger\"{/a}"

    scene bg club with dissolve
    $ show_messenger()

    $ msg ("Hi. What's up?", who=1, status='offline')

    $ show_tooltip()
    $ msg ("Hi, nothing much. Are you still here?")
    $ msg ("Yeah, look at the cool raven.", who=1, status='online')
    
    $ msg (None, who=1, pic="raven")
    $ msg (None, who=1, audio="raven", audio_bar=3)
    
    $ show_tooltip(n=2)
    $ msg ("Nothing much. The crow is cool too.")
    $ msg (None, pic="crow")

    $ msg ("What do you think about our opening?")
    $ msg ("It's from the upcoming VN 'd20: Sweet Roll Club'")
    $ msg (None, audio="opening")
    $ msg ("Give me a couple of minutes.", who=1)

    $ hide_messenger()
    $ time_update(m=2) # plus 2 minutes if the time is not current
    nm "*a few minutes later*"
    $ show_messenger()

    $ msg ("I like it.", who=1)
    $ msg ("I am pleased.")
    $ msg ("What are you doing tonight?")
    
    $ park = False
    $ movie = False 
    
    $ msg (None, choices={0:{'jump':'park', 'name':"Maybe go to the park?"}, 1:{'jump':'movie', 'name':"We could go to the movies."}})

label park:
    python:
        park = True
        msg ("Maybe go to the park?")
        msg ("I am not in the mood for this, [name].", who=1)
        msg ("Okay, next time.")
        msg ("I love {i}poems{/i}.", who=1)

        msg ("Once upon a midnight dreary, while I pondered, weak and weary,\nOver many a quaint and curious volume of forgotten lore —", who=1)
        msg ("While I nodded, nearly napping, suddenly there came a tapping,\nAs of some one gently rapping, rapping at my chamber door —", who=1)
        msg ("«This some visiter», I muttered, «tapping at my chamber door —\nOnly this and nothing more.»", who=1)

        msg ("Farewell.", who=1, status='offline')
        msg ("What do you mean by that?")
        msg ("Where are you?")
        msg ("This is strange.")
    jump end
        
label movie:
    python:
        movie = True
        msg ("We could go to the movies.")
        msg ("Ok. It would be nice.", who=1)
        msg ("I have to go, bye.")
        msg ("Goodbye.")
    jump end

label end:
    $ hide_messenger()

    nm "I turn off my phone."
    if movie:
        nm "I like watching movie."
        "*good end*"
    if park:
        nm "I have to go visit him."
        "*bad end*"

    jump restart

label restart:
    menu:
        "message_time"
        "True":
            $ message_time = True
        "09:41":
            $ message_time = [9,41]
        "False":
            $ message_time = False

    menu:
        "click_to_continue"
        "True":
            $ click_to_continue = True
        "False":
            $ click_to_continue = False
    menu:
        "typewriter"
        "True":
            $ typewriter = True
        "False":
            $ typewriter = False
    menu:
        "interlocutor_typing"
        "True":
            $ interlocutor_typing = True
        "False":
            $ interlocutor_typing = False

    menu:
        "interlocutor_typing_speed"
        "0.05":
            $ interlocutor_typing_speed = 0.05
        "0.1":
            $ interlocutor_typing_speed = 0.1
        "0.3":
            $ interlocutor_typing_speed = 0.3
    $ del_all_msg()
    jump dialogue

#################################################################################
# by sDextra 
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################