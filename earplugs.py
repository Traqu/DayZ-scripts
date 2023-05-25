from pycaw.pycaw import AudioUtilities
import keyboard
from functools import partial
import threading

dayzProcessName = "DayZ_x64.exe"
earplugsEnabled = threading.Event()
volume = 1

sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    if session.Process and session.Process.name() == dayzProcessName:
        dayzSession = session
        print(dayzSession.Process)
        volume_ctrl = dayzSession.SimpleAudioVolume

def enableEarplugs(enableButton):
    if not earplugsEnabled.is_set():
        if enableButton.name == 'n':
            earplugsEnabled.set()
            print("Earplugs enabled")
    else:
        if enableButton.name == 'n':
            earplugsEnabled.clear()
            print("Earplugs disabled")

def setVolume(volumeButton, volume_ctrl):
        global volume
        if(earplugsEnabled.is_set()):
            if volumeButton.name == '=':
                if volume < 1:
                    volume += 0.1
                    volume_ctrl.SetMasterVolume(volume, None)
                    print("Volume set to: " + str(volume))
                    return volume
            elif volumeButton.name == '-':
                if volume > 0:
                    volume -= 0.1
                    volume_ctrl.SetMasterVolume(volume, None)
                    print("Volume set to: " + str(volume))
                    return volume
        

keyboard.on_press(partial(enableEarplugs))
keyboard.on_press(partial(setVolume, volume_ctrl = volume_ctrl))

while True:
    if keyboard.is_pressed('end'):
        break

print("exit 0")
