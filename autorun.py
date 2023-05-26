import keyboard

def on_press(event):
    if event.name == '+':
        keyboard.press('w')
        keyboard.press('shift')


def release(event):
    if event.name == 's' or event.name == 'a' or event.name == 'd' or event.name == 'w':
        keyboard.release('w')
        keyboard.release('shift')


keyboard.on_press(on_press)
    # keyboard.on_release(release)

keyboard.wait('esc')