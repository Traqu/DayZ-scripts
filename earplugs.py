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

def enableEarplugs(event):
    if not earplugsEnabled.is_set():
        if event.name == 'n':
            earplugsEnabled.set()
            print("Earplugs enabled")
    else:
        if event.name == 'n':
            earplugsEnabled.clear()
            print("Earplugs disabled")

def setVolume(event, volumeButton):
    if event.name == volumeButton:
        if volumeButton == '+':
            if volume < 1:
                volume += 0.1
                volume_ctrl.SetMasterVolume(volume, None)
                print("Volume set to: " + str(volume))
        elif volumeButton == '-':
            if volume > 0:
                volume -= 0.1
                volume_ctrl.SetMasterVolume(volume, None)
                print("Volume set to: " + str(volume))

# Ustawienia skrótów klawiszowych
keyboard.on_press(partial(enableEarplugs))
keyboard.on_press(partial(setVolume, volumeButton='+'))
keyboard.on_press(partial(setVolume, volumeButton='-'))

# Pętla nieskończona, czeka na wciśnięcie klawisza 'q' do zakończenia programu
while True:
    if keyboard.is_pressed('q'):
        break

print("exit 0")
