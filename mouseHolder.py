
#IMPORTS#
import time, math, pyautogui, threading, keyboard


#VARIABLES#
MOUSE_MOVE_TRESHOLD = 250
ENTER_ANIMATION_TRESHOLD: time = 3
MINUTE: time = 60
TIME_TEST: time = 3
TIME_5_MIN: time = 60 * 5
TIME_15_MIN: time = TIME_5_MIN * 3
TIME_20_MIN: time = TIME_5_MIN * 4
TIME_30_MIN: time = TIME_5_MIN * 6
COUNTDOWN: time = 5
PLAYER_MOVEMENT_KEYS = ['a','w','d','s','space']
forceExit = False
playerMoved = False
awaitPlayerDecission = True
sawingWasInterrupted = False

#MAIN#
def main():
    
    if not(sawingWasInterrupted):
        acceptUserInput()
    print("\nYou have now 5 seconds to focus on the game.\n")
    time.sleep(1)
    countdown(COUNTDOWN)
    
    for key in PLAYER_MOVEMENT_KEYS:
        keyboard.on_press_key(key, terminateProcess)
    keyboard.on_press_key("esc", terminateProcess)
    
    monitorMouseMovement_thread = threading.Thread(target=monitorMouseMovement)
    monitorPlayerMovement_thread = threading.Thread(target=monitorPlayerMovement)
    monitorMouseMovement_thread.start()
    monitorPlayerMovement_thread.start()
    
    monitorProgress_thread = threading.Thread(target=monitorProgress, args=[cycles, timeForCycle])
    

    print("Holding button began")
    holdButton(cycles, timeForCycle, monitorProgress_thread)

    



#DEFINITIONS#
def holdButton(cycles, timeToWait, monitorProgress_thread):
    monitorProgress_thread.start()
    pyautogui.mouseDown()
    countdown(cycles*timeForCycle)
    pyautogui.mouseUp()
    print("Button released")
    
def countdown(countdown):
    if(countdown==COUNTDOWN):
        while(countdown!=0):
            print("Time left to focus on DayZ: ", countdown)
            countdown-=1
            time.sleep(1)
    else:
        countdown = countdown * MINUTE + ENTER_ANIMATION_TRESHOLD
        while(countdown!=0 and not forceExit):
            print("Time left: ", countdown, "seconds")
            #print("Time left to close the circle: ", countdown)
            countdown-=1
            time.sleep(1)

def monitorMouseMovement():
    global forceExit, sawingWasInterrupted
    monitorMouseMovement = True
    while(monitorMouseMovement is True and not forceExit):
        startingMousePosition = pyautogui.position()
        time.sleep(0.2)
        currentMousePosition = pyautogui.position()
       # print(startingMousePosition)
       # print(currentMousePosition)
        distance = countDistanceBetweenPoints(startingMousePosition, currentMousePosition)
       # print("Distance:", distance)
        if not (keyboard.is_pressed('alt')):
            if(distance > MOUSE_MOVE_TRESHOLD):
                print("Mouse has been moved more than " + str(MOUSE_MOVE_TRESHOLD) + " units → [" + str(distance) + "], and ALT was not being held.")
                monitorMouseMovement = False
                forceExit = True
                sawingWasInterrupted = True

def monitorPlayerMovement():
    global forceExit, sawingWasInterrupted
    monitorPlayerMovement = True
    while(monitorPlayerMovement is True and not forceExit):
        time.sleep(0.05)
        if(playerMoved):    
            monitorPlayerMovement = False
            forceExit = True
            sawingWasInterrupted = True

def countDistanceBetweenPoints(startingMousePosition, currentMousePosition):
    distance = math.sqrt((startingMousePosition.x - currentMousePosition.x)**2 + (startingMousePosition.y - currentMousePosition.y)**2)
    return distance

def acceptUserInput():
    global cycles, timeForCycle
    valid = False
    while(not valid):
        cycles = input("Type in how many cycles is required to crack the codelock: ")
        try:
            cycles = int(cycles)
            valid = True
        except:
            print("Input must be an Integer value")

    valid = False

    while(not valid):
        timeForCycle = input("Type in how long does one cycle take (in minutes): ")
        try:
            timeForCycle = int(timeForCycle)
            valid = True
        except:
            print("Input must be an Integer value")
    
def monitorProgress(cycles, timeForCycle):
    while(not forceExit):
       #TODO update on progress
       time.sleep(0.1)
    
def terminateProcess(key_pressed):
    global forceExit, playerMoved
    if (awaitPlayerDecission):
        if(key_pressed.name == 'esc'):
            print("The process was forcibly frozen due to pressing the ESC key.")
            forceExit = True
        else:
            playerMoved = True
            print("Interruption of the process due to Player movement.")
            forceExit = True
        

    
# START #            
main()
while awaitPlayerDecission:
    time.sleep(0.1)
    if forceExit:
        awaitPlayerDecission = False
        continueSawing = input("\nIf you wish to continue what was interrupted, type 'y' or 'yes' and press Enter.\nAny other input will fully terminate the process: ")
        continueSawing = "".join(continueSawing.split())
        if continueSawing in ["y", "ye", "yes", "Y", "YE", "YES"]:
            continueSawing = True
        else:
            continueSawing = False
    elif (not awaitPlayerDecission):
        awaitPlayerDecission = True
        forceExit = False
    #TODO process will run new main if you want to continue    
            
print("Program has closed.")