from pycaw.pycaw import AudioUtilities
import keyboard
from functools import partial
import threading
import time

dayzProcessName = "DayZ_x64.exe"
earplugsEnabled = threading.Event()
volume = 1
dayzSession = None
escape_pressed = False
allow_exit = True
volume_ctrl = None
shift_pressed = False
n_pressed = False

print("\n\nTo exit the application press ESC")

def on_escape_press(event):
    global escape_pressed, allow_exit
    if dayzSession is None:
        escape_pressed = True
    elif allow_exit:
        allow_exit = False
        print("Escape key pressed. Exiting...")
    else:
        print("To exit - press END.")


def on_shift_press(event):
    global shift_pressed
    shift_pressed = True

def on_shift_release(event):
    global shift_pressed
    shift_pressed = False
    
def on_n_press(event):
    global n_pressed
    n_pressed = True

def on_n_release(event):
    global n_pressed
    n_pressed = False
    
keyboard.on_press_key("esc", on_escape_press)
keyboard.on_press_key("shift", on_shift_press)
keyboard.on_release_key("shift", on_shift_release)
keyboard.on_press_key("n", on_n_press)
keyboard.on_release_key("n", on_n_release)

while dayzSession is None and not escape_pressed:
    try:
        print("\nAwaiting for DayZ to start up...")
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == dayzProcessName:
                dayzSession = session
                print("\nConnection established:\n" + str(dayzSession.Process))
                volume_ctrl = dayzSession.SimpleAudioVolume
                break
            else:
                time.sleep(0.1)
                print("Trying to link DayZ process to the audio controller...")
                if escape_pressed:
                    break
        if(volume_ctrl is None):
            time.sleep(5)
    

    except Exception as e:
        print("Error occurred:", str(e))
        break

if(volume_ctrl is not None):
    print("\nDayZ audio controller has been succesfully linked!\nYou can enable your earplugs by pressing 'N' button now.\n\n")

if escape_pressed:
    print("Escape key pressed. Exiting...")
else:
    def enableEarplugs(enableButton):
        if not earplugsEnabled.is_set():
            if enableButton.name == 'n' or n_pressed and shift_pressed:
                earplugsEnabled.set()
                print("Earplugs enabled")
                volume_ctrl.SetMasterVolume(volume, None)
        else:
            if enableButton.name == 'n' or n_pressed and shift_pressed:
                earplugsEnabled.clear()
                print("Earplugs disabled")
                volume_ctrl.SetMasterVolume(1, None)

    def setVolume(volumeButton, volume_ctrl):
        global volume
        if earplugsEnabled.is_set():
            if volumeButton.name == '=' or volumeButton.name == '+':
                if volume < 1:
                    volume += 0.1
                    volume = round(volume, 1)
                    volume_ctrl.SetMasterVolume(volume, None)
                    print("Volume set to: " + str(volume))
            elif volumeButton.name == '-' or volumeButton.name == '_':
                if volume > 0:
                    volume -= 0.1
                    volume = round(volume, 1)
                    volume_ctrl.SetMasterVolume(volume, None)
                    print("Volume set to: " + str(volume))

    keyboard.on_press(partial(enableEarplugs))
    keyboard.on_press(partial(setVolume, volume_ctrl=volume_ctrl))

    while True:
        if keyboard.is_pressed('end') or escape_pressed:
            break

if(volume_ctrl is not None):
    volume_ctrl.SetMasterVolume(1, None)
print("Exiting application")