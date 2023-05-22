import time
import keyboard
import datetime

#####################################################################################
#####################################################################################
#####################################################################################

server_hold_time_10 = 4.2 # zmienić jeśli serwer wymaga innego czasu przytrzymania...
server_hold_time_1 = 1.2 # zmienić jeśli serwer wymaga innego czasu przytrzymania...

countDownTimer = 3
TIME_NEEDED_TO_EXIT_ANIMATION = 0.7
DELAY_BETWEEN_COMMANDS = 0.2

#####################################################################################

def get_time():
    return datetime.datetime.now().time().strftime("%H:%M:%S")

#####################################################################################


def press_and_hold_key(key, hold_time):
    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

#####################################################################################

def from_thousands_to_ones():
    print(get_time() + '  From thousands to ones')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(3):
        press_and_hold_key('f', 0.1)

def from_hundreeds_to_ones():
    print(get_time() + '  From hundreeds to ones')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(2):
        press_and_hold_key('f', 0.1)    

def from_hundreeds_to_tens():
    print(get_time() + '  From hundreeds to tens')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    press_and_hold_key('f', 0.1)    

def from_tens_to_ones():
        print(get_time() + '  From tens to ones')
        # konieczne żeby poczekać na wyjście z poprzedniej animacji
        time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
        press_and_hold_key('f', 0.1)      

def from_ones_to_tens():
    print(get_time() + '  From ones to tens')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(3):
        press_and_hold_key('f', 0.1)

def from_ones_to_hundreeds():
    print(get_time() + '  From ones to hundreeds')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(2):
        press_and_hold_key('f', 0.1)

def from_ones_to_thousands():
    print(get_time() + '  From ones to thousands')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    press_and_hold_key('f', 0.1)

#####################################################################################
#####################################################################################

def increment():
    print(get_time() + '  Increment')
    press_and_hold_key('f', server_hold_time_1)    

def setup():
    from_thousands_to_ones()

#####################################################################################
#####################################################################################

def check_0001s_options(key, hold_time):
    print(get_time() + '  Checking ones')
    press_and_hold_key('f', server_hold_time_10)
   # time.sleep(1.0)

def check_0010s_options():
    for _ in range(10):
         check_0001s_options('f', server_hold_time_10)
         from_ones_to_tens()
         increment()
         from_tens_to_ones()

def check_0100s_options():
    for _ in range(10):
      from_ones_to_hundreeds()
      increment()
      from_hundreeds_to_ones()
      check_0010s_options()
 #  from_ones_to_hundreeds()
 #  increment()
 #  from_hundreeds_to_tens()
 #  increment()
 #  from_tens_to_ones()

def check_1000s_options():
    for _ in range(10):
        from_ones_to_thousands()
        increment()
        from_thousands_to_ones()
        check_0100s_options()
       # for _ in range(10):
         #   check_0010s_options()
         #   check_0001s_options('f', server_hold_time_10)
         #   check_0100s_options()

#####################################################################################
#####################################################################################

def start_cracking_the_code():

   setup() #starting pos. from ones (player runs the script at thousands)

 #  check_0010s_options()
 #  check_0100s_options()
   check_1000s_options()



#####################################################################################
#####################################################################################
#####################################################################################

time.sleep(0.75)  # Oczekiwanie na przeniesienie focusu na DayZ
print("\n\nAwaiting to focus at DayZ...")
time.sleep(1.0)

print('\nStarting in: ')
time.sleep(1)
for x in range(0, 3):
    print(str(countDownTimer) + "...")
    countDownTimer=countDownTimer-1
    time.sleep(1)
time.sleep(0.5)
print('\n' + get_time() + '  \nCRACKING IS BEING PERFORMED!\n')

start_time = time.time()
start_cracking_the_code()
end_time = time.time()


print(get_time() + "Lock opening finished.")
execution_time = end_time - start_time
print("Script execution time:", execution_time, "seconds")

#####################################################################################