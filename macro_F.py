import time
import keyboard

#####################################################################################
#####################################################################################
#####################################################################################

server_hold_time_10 = 4.1 # zmienić jeśli serwer wymaga innego czasu przytrzymania...
server_hold_time_1 = 1.2 # zmienić jeśli serwer wymaga innego czasu przytrzymania...

countDownTimer = 3
TIME_NEEDED_TO_EXIT_ANIMATION = 0.5
DELAY_BETWEEN_COMMANDS = 0.1

#####################################################################################

def press_and_hold_key(key, hold_time):
    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

#####################################################################################

def from_thousands_to_ones():
    print('From thousands to ones')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(3):
        press_and_hold_key('f', 0.05)

def from_hundreeds_to_ones():
    print('From hundreeds to ones')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(2):
        press_and_hold_key('f', 0.05)    

def from_hundreeds_to_tens():
    print('From hundreeds to tens')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    press_and_hold_key('f', 0.05)    

def from_tens_to_ones():
        print('From tens to ones')
        # konieczne żeby poczekać na wyjście z poprzedniej animacji
        time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
        press_and_hold_key('f', 0.05)      

def from_ones_to_tens():
    print('From ones to tens')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(3):
        press_and_hold_key('f', 0.05)

def from_ones_to_hundreeds():
    print('From ones to hundreeds')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    for _ in range(2):
        press_and_hold_key('f', 0.05)

def from_ones_to_thousands():
    print('From ones to thousands')
    time.sleep(TIME_NEEDED_TO_EXIT_ANIMATION)
    press_and_hold_key('f', 0.05)

#####################################################################################
#####################################################################################

def increase_by_one():
    print('Increment')
    press_and_hold_key('f', server_hold_time_1)    

def setup():
    from_thousands_to_ones()

#####################################################################################
#####################################################################################

def check_0001s_options(key, hold_time):
    print('Checking ones')
    press_and_hold_key('f', server_hold_time_10)
    time.sleep(1.0)

def check_0010s_options():
    for _ in range(10):
         check_0001s_options('f', server_hold_time_10)
         from_ones_to_tens()
         increase_by_one()
         from_tens_to_ones()    

def check_0100s_options():
    for _ in range(10):
      from_ones_to_hundreeds()
      increase_by_one()
      from_hundreeds_to_ones()
      check_0010s_options()
  #  from_ones_to_hundreeds()
  #  increase_by_one()
  #  from_hundreeds_to_tens()
  #  increase_by_one()
  #  from_tens_to_ones()

def check_1000s_options():
    for _ in range(10):
        from_ones_to_thousands()
        increase_by_one()
        from_thousands_to_ones()
        for _ in range(10):
            check_0010s_options()
            check_0001s_options('f', server_hold_time_10)
            check_0100s_options()

#####################################################################################
#####################################################################################

def start_cracking_the_code():

   setup() #starting pos. from ones (player runs the script at thousands)

   check_0010s_options()
   check_0100s_options()
   check_1000s_options()

#####################################################################################
#####################################################################################
#####################################################################################

time.sleep(0.75)  # Oczekiwanie na przeniesienie focusu na DayZ
print("\n\n\nOczekiwanie na przeniesienie focusu na DayZ...")
time.sleep(1.0)

print('\nStarting in: ')
time.sleep(1)
for x in range(0, 3):
    print(str(countDownTimer) + "...")
    countDownTimer=countDownTimer-1
    time.sleep(1)
print('Start!')
time.sleep(0.5)
print('\nCRACKING IS BEING PERFORMED!\n')

start_cracking_the_code()

print("Zakończono otwieranie zamków.")

#####################################################################################