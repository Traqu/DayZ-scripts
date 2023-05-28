import keyboard
import time
import mouse

AUTORUN_BUTTON = 'pause'
HOTKEYS_W_AR = 'w + ' + AUTORUN_BUTTON
HOTKEYS_SHIFT_W_AR = 'shift + w + ' + AUTORUN_BUTTON
is_running = False
w_pressed = False
autorun_hotkey_detected = False
inventory_opened = False

def release_tab(dummy_arg=None):
    if(is_running):
        keyboard.release('tab')

def autorun():
    keyboard.press('w')
    keyboard.press('shift')

def start_autorun(dummy_arg=None):
    global autorun_hotkey_detected
    global is_running
    if(not autorun_hotkey_detected):
        is_running = True
        autorun()
    else:
        autorun_hotkey_detected = False

def start_autorun__giveaway_control(dummy_arg=None):
    global autorun_hotkey_detected
    global is_running
    autorun_hotkey_detected = True
    time.sleep(0.18)
    is_running = True
    autorun()

def overtake_control(dummy_arg=None):
    global is_running
    if is_running:
        is_running = False
        keyboard.release('shift')

def force_stop_autorun(stop_button = None):
    global is_running
    if is_running:
        if(stop_button is not None):
            if(not stop_button.name == 'esc'):
                is_running = False
                keyboard.release('w')
                keyboard.release('shift')
            else:
                if(not inventory_opened):
                    is_running = False
                    keyboard.release('w')
                    keyboard.release('shift')
        else:
            if(not inventory_opened):
                is_running = False
                keyboard.release('w')
                keyboard.release('shift')
            

# ↓ possible that Steam detects the hotkeys faster no matter what - ↓
# - seem to be working 1/3 of the times (and maybe only in 1st attempt also - carry out thorough testing)
def overlay_buttons_stop_autorun(overlay_button):
    global is_running, inventory_opened
    if is_running:
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
        is_running = False
        time.sleep(0.1)
        start_autorun()
    

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


while True:
    if is_running:
        if not w_pressed and keyboard.is_pressed('w'):
            w_pressed = True
            is_running = False
    time.sleep(0.1)