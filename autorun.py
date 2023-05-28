import keyboard
import time
import mouse

AUTORUN_BUTTON = 'pause'
HOTKEYS_W_AR = 'w + ' + AUTORUN_BUTTON
HOTKEYS_SHIFT_W_AR = 'shift + w + ' + AUTORUN_BUTTON
is_running = False
w_pressed = False
autorun_hotkey_detected = False

def autorun():
    print("Autorun enabled: " + str(is_running).upper())
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

def force_stop_autorun(dummy_arg=None):
    global is_running
    if is_running:
        is_running = False
        keyboard.release('w')
        keyboard.release('shift')

def on_w_release(e):
    global w_pressed
    if e.name == 'w':
        w_pressed = False
        
        
keyboard.on_press_key('pause', start_autorun)
keys_to_stop = ['s', 'a', 'd', 'esc', 'win', 'ctrl']

for key in keys_to_stop:
    keyboard.on_press_key(key, force_stop_autorun)
    
keyboard.on_release_key('w', on_w_release)
keyboard.on_press_key('w', overtake_control)
keyboard.add_hotkey(HOTKEYS_W_AR, start_autorun__giveaway_control)
keyboard.add_hotkey(HOTKEYS_SHIFT_W_AR, start_autorun__giveaway_control)
mouse.on_right_click(force_stop_autorun)

while True:
    if is_running:
        if not w_pressed and keyboard.is_pressed('w'):
            w_pressed = True
            is_running = False
            print("Autorun enabled: " + str(is_running).upper())
    time.sleep(0.1)