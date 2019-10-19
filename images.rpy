#################################################################################
# by sDextra 
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################
init -1000 python:
    ### Color Scheme
    style_green = '#2CB42C'
    style_gray = '#6d7b85'
    style_button_back = '#282E33' 
    style_button_hovr = '#5F6C77'
    style_button_inst = '#14171A'
    style_font = 'fonts/tahoma.ttf'
    style_font_monospace = 'fonts/hack.ttf'

init python:
    # Button Style
    style.btn = Style(style.default)
    style.btn.background = style_button_back
    style.btn.hover_background = style_button_hovr
    style.btn.insensitive_background = style_button_inst
    # Bar Style
    style.bar_vert = Style(style.default)
    style.bar_vert.right_bar = style_button_inst 
    style.bar_vert.left_bar = style_button_inst 
    style.bar_vert.thumb = style_button_hovr
    style.bar_vert.bar_vertical = True
    style.bar_vert.bar_invert = True
    style.bar_vert.align = (1.0,0.6)
    style.bar_vert.xysize = (10,780)
    # Text Style
    style.txt_base = Style(style.default)
    style.txt_base.font = style_font
    style.txt_base.xalign = 0.5
    style.txt_base.yalign = 0.5
    style.txt_base.size = 28
    style.txt_base.color = '#fff'
    # Time Style
    style.txt_time = Style(style.txt_base)
    style.txt_time.align = (1.0,.98)
    style.txt_time.xanchor = 1.0
    style.txt_time_gc = Style(style.txt_time)
    style.txt_time_gc.xpos = 40
    # Status Style
    style.txt_status = Style(style.txt_base)
    style.txt_status.size = 24
    style.txt_status.color = style_green
    style.txt_status.font = style_font_monospace

    def color_brightness(image, b=0.2):
        return im.MatrixColor(image, im.matrix.brightness(b))
    def color_saturation(image, b=-0.05):
        return im.MatrixColor(image, im.matrix.saturation(b))

init:
    transform move_messenger(t=1.0):
        xalign .9 yalign .5
        on show:
            xalign 1.5 
            easein t xalign 0.9
        on hide:
            easeout t xalign 1.5
            alpha 0

    transform move_pic(t=.5):
        xalign .5 yalign .5
        on show:
            yalign -2.0
            easein t yalign .5
        on hide:
            easeout t yalign -2.0
            alpha 0

    transform move_tooltip():
        xalign 0.0 yalign .05
        on show:
            xalign -0.8 yalign 0.05
            easein 1.0 xalign 0.0
        on hide:
            easeout 1.0 xalign -0.8
            alpha 0

    transform blackout():
        alpha 1
        on show:
            alpha 0
            easein .5 alpha 1
        on hide:
            easeout .5 alpha 0
image empty = '#00000000'

image status_typing_groupchat:
    Text(active_groupchat.get_interlocutor(groupchat_who_typing).name+' typing.  ', style='txt_status')
    pause 0.2
    Text(active_groupchat.get_interlocutor(groupchat_who_typing).name+' typing.. ', style='txt_status')
    pause 0.2
    Text(active_groupchat.get_interlocutor(groupchat_who_typing).name+' typing...', style='txt_status')
    pause 0.2
    Text(active_groupchat.get_interlocutor(groupchat_who_typing).name+' typing.. ', style='txt_status')
    pause 0.2
    repeat

image status_picture_groupchat:
    Text(active_groupchat.get_interlocutor(groupchat_who_typing).name+' sends a picture', style='txt_status')
image status_audio_groupchat:
    Text(active_groupchat.get_interlocutor(groupchat_who_typing).name+' sends an audio', style='txt_status')


image status_online:
    Text('online', style='txt_status')
image status_picture:
    Text('sends a picture', style='txt_status')
image status_audio:
    Text('sends an audio', style='txt_status')
image status_typing:
    Text('typing.  ', style='txt_status')
    pause 0.2
    Text('typing.. ', style='txt_status')
    pause 0.2
    Text('typing...', style='txt_status')
    pause 0.2
    Text('typing.. ', style='txt_status')
    pause 0.2
    repeat
image status_offline:
    Text('last seen recently', style='txt_status', color='#6d7b85')


init python:
    # HUD
    def dn_hud(st, at):
        return color_theme('images/messenger/hud.png'), 0.1
    # BACK
    def dn_back(st, at):
        return color_theme('images/messenger/back.png'), 0.1
    # BOXES
    def dn_box(st, at):
        return color_theme('images/messenger/box.png'), 0.1
    def dn_box_hv(st, at):
        return color_theme(color_brightness('images/messenger/box.png')), 0.1
    def dn_box_two(st, at):
        return color_theme('images/messenger/box_two.png'), 0.1
    def dn_box_two_hv(st, at):
        return color_theme(color_brightness('images/messenger/box_two.png')), 0.1
    # BUTTONS
    def dn_arr(st,at):
        return color_theme('images/messenger/arrow.png'), 0.1
    def dn_arr_hv(st,at):
        return color_theme(color_brightness('images/messenger/arrow.png')), 0.1
    def dn_oth(st,at):
        return color_theme('images/messenger/other.png'), 0.1
    def dn_oth_hv(st,at):
        return color_theme(color_brightness('images/messenger/other.png')), 0.1
    def dn_mgn(st,at):
        return color_theme('images/messenger/magnifier.png'), 0.1
    def dn_mgn_hv(st,at):
        return color_theme(color_brightness('images/messenger/magnifier.png')), 0.1
    # AUDIO
    def dn_pl(st,at):
        return color_theme('images/messenger/audio/play.png'), 0.1
    def dn_pl_hv(st,at):
        return color_theme(color_brightness('images/messenger/audio/play.png')), 0.1
    def dn_st(st,at):
        return color_theme('images/messenger/audio/stop.png'), 0.1
    def dn_st_hv(st,at):
        return color_theme(color_brightness('images/messenger/audio/stop.png')), 0.1

    def color_theme(image):
        return im.MatrixColor(image, im.matrix.tint(persistent.theme[0], persistent.theme[1], persistent.theme[2]))
    
    # SET COLOR THEME - RED, GREEN, BLUE (RGB)
    def set_color_theme(rd,gr,bl):
        store.persistent.theme = [rd,gr,bl]
        renpy.restart_interaction()

image arrow_idle = DynamicDisplayable(dn_arr)
image arrow_hover = DynamicDisplayable(dn_arr_hv)

image other_idle = DynamicDisplayable(dn_oth)
image other_hover = DynamicDisplayable(dn_oth_hv)

image magnifier_idle = DynamicDisplayable(dn_mgn)
image magnifier_hover = DynamicDisplayable(dn_mgn_hv)

image messenger_hud = DynamicDisplayable(dn_hud) 
image messenger_back = DynamicDisplayable(dn_back) 
image box_one = DynamicDisplayable(dn_box)
image hover_box = DynamicDisplayable(dn_box_hv)
image box_two = DynamicDisplayable(dn_box_two)
image hover_box_two = DynamicDisplayable(dn_box_two_hv)

image play_idle = DynamicDisplayable(dn_pl)
image play_hover = DynamicDisplayable(dn_pl_hv)
image stop_idle = DynamicDisplayable(dn_st)
image stop_hover = DynamicDisplayable(dn_st_hv)

image bg club = 'bg/club.png' # background from the upcoming VN 'd20: Sweet Roll Club'
#################################################################################

#################################################################################
# by sDextra 
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################