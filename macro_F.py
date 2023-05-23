import time
import keyboard
import datetime
import threading
import pyautogui

#####################################################################################

server_hold_time_10 = 6.33 # zmienić jeśli serwer wymaga innego czasu przytrzymania...
server_hold_time_1 = 1.55  # zmienić jeśli serwer wymaga innego czasu przytrzymania...

countDownTimer = 5
TIME_NEEDED_TO_EXIT_ANIMATION = 0.6
DELAY_BETWEEN_COMMANDS = 0.1 # DO NOT TOUCH!
FROM_TO__HOLD_TIME = 0.0825
BUTTON = 'f'

exit_key = None

#####################################################################################

def get_time():
    return datetime.datetime.now().time().strftime("%H:%M:%S")


def format_time(execution_time):
    execution_time_formatted = "{:.2f}".format(execution_time)
    return execution_time_formatted

#####################################################################################

def press_and_hold_key(key, hold_time):
    if stop_flag.is_set():
        return
    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

#####################################################################################

def from_thousands_to_ones():
    if stop_flag.is_set():
        return
    print(get_time() + '  From thousands to ones')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(3):
        press_and_hold_key(BUTTON, FROM_TO__HOLD_TIME)

def from_hundreeds_to_ones():
    if stop_flag.is_set():
        return
    print(get_time() + '  From hundreeds to ones')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(2):
        press_and_hold_key(BUTTON, FROM_TO__HOLD_TIME)

def from_hundreeds_to_tens():
    if stop_flag.is_set():
        return
    print(get_time() + '  From hundreeds to tens')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    press_and_hold_key(BUTTON, FROM_TO__HOLD_TIME)

def from_tens_to_ones():
    if stop_flag.is_set():
        return
    print(get_time() + '  From tens to ones')
    # konieczne żeby poczekać na wyjście z poprzedniej animacji
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    press_and_hold_key(BUTTON, FROM_TO__HOLD_TIME)

def from_ones_to_tens():
    if stop_flag.is_set():
        return
    print(get_time() + '  From ones to tens')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(3):
        press_and_hold_key(BUTTON, FROM_TO__HOLD_TIME)

def from_ones_to_hundreeds():
    if stop_flag.is_set():
        return
    print(get_time() + '  From ones to hundreeds')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(2):
        press_and_hold_key(BUTTON, FROM_TO__HOLD_TIME)

def from_ones_to_thousands():
    if stop_flag.is_set():
        return
    print(get_time() + '  From ones to thousands')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    press_and_hold_key(BUTTON, FROM_TO__HOLD_TIME)

#####################################################################################

def increment():
    if stop_flag.is_set():
        return
    print(get_time() + '  Increment')
    press_and_hold_key(BUTTON, server_hold_time_1)


def setup():
    from_thousands_to_ones()

#####################################################################################

def check_0001s_options(key, hold_time):
    if stop_flag.is_set():
        return
    print(get_time() + '  Checking ones')
    press_and_hold_key(BUTTON, server_hold_time_10)
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    if pyautogui.locateOnScreen('f.png',confidence=0.85)==None:
        stop_flag.set()
        print("I have found the code!")
        return
    else:
        print("I still haven't found the code")

def check_0010s_options():
    for _ in range(10):
        check_0001s_options(BUTTON, server_hold_time_10)
        from_ones_to_tens()
        increment()
        from_tens_to_ones()

def check_0100s_options():
    for _ in range(10):
        from_ones_to_hundreeds()
        increment()
        from_hundreeds_to_ones()
        check_0010s_options()

def check_1000s_options():
    if stop_flag.is_set():
        return
    for _ in range(10):
        if stop_flag.is_set():
            return
        from_ones_to_thousands()
        increment()
        from_thousands_to_ones()
        check_0100s_options()

#####################################################################################
#####################################################################################

# Tworzymy flagę, która będzie służyć do przerwania metody start_cracking_the_code()
stop_flag = threading.Event()

def stop_execution():
    stop_flag.set()

# Funkcja obsługująca wciśnięcie klawisza
def key_press_handler(event):
    global exit_key
    if event.name == 'a' or event.name == 'w' or event.name == 's' or event.name == 'd' or event.name == 'esc' or event.name == 'space' or event.name == 'shift':
        exit_key = event.name
        stop_execution()

# Rejestrujemy funkcję obsługującą wciśnięcie klawisza przerywającego proces
keyboard.on_press(key_press_handler)

def start_cracking_the_code():
    setup()  # starting pos. from ones (player runs the script at thousands)
    check_1000s_options()
    if stop_flag.is_set():
        if exit_key!=None:
            print("\nScript has been cancelled due to - " + exit_key.upper() + " - pressing\n")
        else:
            print("\nScript has been cancelled due to succesfull code breach\n")
        return

#####################################################################################
#####################################################################################

time.sleep(0.6)
print('Keys that will terminate the script: ESC, SPACE, SHIFT, A, W, D, S')

time.sleep(1.4)  # Oczekiwanie na przeniesienie focusu na DayZ
print("\n\nAwaiting to focus at DayZ...\nDo not perform any moves in game")
time.sleep(1.0)

print('\nStarting in: ')
time.sleep(1)
for x in range(0, countDownTimer):
    print(str(countDownTimer) + "...")
    countDownTimer = countDownTimer - 1
    time.sleep(1)
time.sleep(0.5)
print('\n' + get_time() + ' EXECUTION START TIME - it might take up to 3 hours to fulfill\n\n\nCRACKING LOGS:\n')

start_time = time.time()
start_cracking_the_code()
end_time = time.time()

print(get_time() + "  Lock opening finished.\n")
execution_time = end_time - start_time

execution_time_formatted = format_time(execution_time)

print("Script execution time:", execution_time_formatted, "sedonds")
print("Script execution time:", format_time(execution_time / 60), "minutes (decimal)")
print("Script execution time:", format_time(execution_time / 60 / 60), "hours (decimal)")
time.sleep(5)
print("\nClosing the process")
time.sleep(2)