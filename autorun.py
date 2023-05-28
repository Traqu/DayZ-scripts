import keyboard
import time
import mouse

AUTORUN_BUTTON = 'pause'
HOTKEYS_W_AR = 'w + ' + AUTORUN_BUTTON
HOTKEYS_SHIFT_W_AR = 'shift + w + ' + AUTORUN_BUTTON
autorun_enabled = False
w_pressed = False
autorun_hotkey_detected = False
inventory_opened = False
map_enabled = False
should_you_let_me_in = False
enter_pressed = False

def handle_chat(chat_button):
    global enter_pressed, autorun_enabled
    autorun_enabled = False
    keyboard.release('w')
    keyboard.release('shift')
    
   # if(autorun_enabled):
   #     autorun_enabled = False
    
#    if(autorun_enabled):
#        keyboard.release('w')
#        keyboard.release('shift')
#        enter_pressed = True
#        autorun_enabled = False
#    elif(enter_pressed):
#        print("ZAKURWIAMY DALEJ")
#        time.sleep(0.1)
#        autorun()
#        enter_pressed = False


def handle_map_button(map_button):
    global map_enabled, should_you_let_me_in
    if(autorun_enabled or should_you_let_me_in):
        if(not map_enabled):
           force_stop_autorun()
           map_enabled = True
           should_you_let_me_in = True
        else:
            time.sleep(0.05)
            start_autorun(event=None)
            map_enabled = False 
            should_you_let_me_in = False

def release_tab(event):
    if(autorun_enabled):
        keyboard.release('tab')

def autorun():
    keyboard.press('w')
    keyboard.press('shift')
    print("Autorun enabled: " + str(autorun_enabled))

def start_autorun(event):
    global autorun_hotkey_detected, autorun_enabled
    if(not autorun_hotkey_detected):
        autorun_enabled = True
        autorun()
    else:
        autorun_hotkey_detected = False

def start_autorun__giveaway_control():
    global autorun_hotkey_detected
    global autorun_enabled
    autorun_hotkey_detected = True
    time.sleep(0.18)
    autorun_enabled = True
    autorun()

def overtake_control(event):
    global autorun_enabled
    if autorun_enabled:
        autorun_enabled = False
        keyboard.release('shift')

def force_stop_autorun(stop_button = None):
    global autorun_enabled
    if autorun_enabled:
        if(stop_button is not None):
            if(not stop_button.name == 'esc'):
                autorun_enabled = False
                keyboard.release('w')
                keyboard.release('shift')
            else:
                if(not inventory_opened):
                    autorun_enabled = False
                    keyboard.release('w')
                    keyboard.release('shift')
        else:
            if(not inventory_opened):
                autorun_enabled = False
                keyboard.release('w')
                keyboard.release('shift')
            

# ↓ possible that Steam detects the hotkeys faster no matter what - ↓
# - seem to be working 1/3 of the times (and maybe only in 1st attempt also - carry out thorough testing)
def overlay_buttons_stop_autorun(overlay_button):
    global autorun_enabled, inventory_opened
    if autorun_enabled:
        keyboard.release('tab')
        if(overlay_button.name == 'tab'):
            keyboard.press('tab')
            if(inventory_opened):
                inventory_opened = False
            else:
                inventory_opened = True
        else:
            keyboard.press('`')
            keyboard.release('`')
        keyboard.release('shift')
        keyboard.release('w')
        autorun_enabled = False
        time.sleep(0.1)
        start_autorun(event=None)
    

def on_w_release(e):
    global w_pressed
    if e.name == 'w':
        w_pressed = False
        
        
keyboard.on_press_key('pause', start_autorun)
keys_to_stop = ['s', 'a', 'd', 'esc', 'win', 'ctrl']

for key in keys_to_stop:
    keyboard.on_press_key(key, force_stop_autorun)
    
keyboard.on_press_key('tab', overlay_buttons_stop_autorun)
keyboard.on_press_key('`', overlay_buttons_stop_autorun)
keyboard.on_release_key('w', on_w_release)
keyboard.on_press_key('w', overtake_control)
keyboard.add_hotkey(HOTKEYS_W_AR, start_autorun__giveaway_control)
keyboard.add_hotkey(HOTKEYS_SHIFT_W_AR, start_autorun__giveaway_control)
mouse.on_right_click(force_stop_autorun)
keyboard.on_press(release_tab)
keyboard.on_press_key('m', handle_map_button)
keyboard.on_press_key('enter', handle_chat) 
# to uwidacznia problemy NIEwyłączania sie runa w niektórych sytuacjach (debug)

while True:
    if autorun_enabled:
        if not w_pressed and keyboard.is_pressed('w'):
            w_pressed = True
            autorun_enabled = False
    time.sleep(0.1)