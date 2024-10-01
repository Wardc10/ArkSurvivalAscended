import pyautogui
import pygetwindow as gw
import time
import sys

#wait for input to begin script, ensures user is ready with ASA open before starting
#input("-=-Press any key to run script-=-")

#declare ArkAscended window title name
asa_window_title = 'ArkAscended'

#try to locate the 'ArkAscended' window and make it the active window
try: 
    #Use pygetwindow package to store the ArkAscended window name in asaWindow variable
    asaWindow = gw.getWindowsWithTitle(asa_window_title)[0]

#if no Ark Ascended window currently exists, print error and exit program
except Exception as noArkAscendedWindow:
    print(f"Window titled '{asa_window_title}' not found! Make sure the game is running!")
    sys.exit()

# set asa as the active window since pyautogui only works on the active window
asaWindow.activate() 

# Wait a second to ensure the window is active
time.sleep(1) 

# List of commands to run in ASA console
commands = ['r.VolumetricCloud 0', 'r.VolumetricFog 0', 
            'r.Water.SingleLayer.Reflection 0', 'r.DistanceFieldShadowing 1',
            'grass.sizeScale .33']

# Loop through commands list, entering specified commands/values into in-game console one by one
for i in commands:
# Open in-game console
    pyautogui.press('`')
    # Use pyautogui to type current command into in-game console, interval of 0.05 sec between keystrokes
    pyautogui.write(str(i), interval=0.05)
    # Enter command
    pyautogui.press('enter')
    # Command completion msg
    print(str(i), "Entered..")

# Exit msg
print("All Commands Entered Successfully!")
print("Enjoy Your Time in the ARK!")
sys.exit()