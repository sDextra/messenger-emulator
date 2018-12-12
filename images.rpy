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
    style_font = 'gui/tahoma.ttf'
    style_font_monospace = 'gui/hack.ttf'

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

image messenger_background = 'messenger/back.png'

image arrow_idle = 'images/messenger/arrow.png'
image arrow_hover = color_brightness('images/messenger/arrow.png')

image magnifier_idle = 'images/messenger/magnifier.png'
image magnifier_hover = color_brightness('images/messenger/magnifier.png')

image box_one = 'messenger/box.png'
image hover_box = color_brightness('images/messenger/box.png', b=.1)
image box_two = 'messenger/box_two.png'
image hover_box_two = color_brightness('images/messenger/box_two.png', b=.1)

image play_idle = 'messenger/audio/play.png'
image play_hover = color_brightness('messenger/audio/play.png')
image stop_idle = 'messenger/audio/stop.png'
image stop_hover = color_brightness('messenger/audio/stop.png')

image bg club = 'bg/club.png' # background from the upcoming VN 'd20: Sweet Roll Club'
#################################################################################

#################################################################################
# by sDextra 
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################