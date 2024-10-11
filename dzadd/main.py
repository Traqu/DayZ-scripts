import pyautogui
import time
import keyboard  # Użyj tej biblioteki do detekcji klawiszy

while True:
    if keyboard.is_pressed('esc') or keyboard.is_pressed('end'):
        print("Zamykam aplikację...")
        break  # Zakończ pętlę i wyjdź z programu

    dzl = pyautogui.locateOnScreen("resources/add/graphics/dzl.png", grayscale=True, confidence=0.9)

    if dzl is not None:
        x, y = pyautogui.center(dzl)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.5)  # Krótkie opóźnienie po kliknięciu w dzl

        # Czekaj na pojawienie się check
        while True:
            try:
                check = pyautogui.locateOnScreen("resources/add/graphics/check.png", grayscale=True, confidence=0.8)
                if check is not None:
                    time.sleep(0.5)  # Krótkie opóźnienie, gdy check jest widoczny
                else:
                    break  # Zakończ pętlę, gdy check zniknie
            except pyautogui.ImageNotFoundException:
                break  # Zakończ pętlę, jeśli check nie zostanie znaleziony

        time.sleep(1.5)  # Dodatkowe opóźnienie przed kolejną akcją

    x_image = pyautogui.locateOnScreen("resources/add/graphics/x.png", grayscale=True, confidence=0.95)

    if x_image is not None:
        time.sleep(1)  # Odczekaj sekundę przed kliknięciem
        x, y = pyautogui.center(x_image)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.5)  # Krótkie opóźnienie po kliknięciu w x
