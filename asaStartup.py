import pyautogui

while True:
    #wait for input to begin script, ensures user is ready with ASA open before starting
    input("-=-Press any key to run script-=-") 

    #list of commands to run in ASA console
    commands = ['r.VolumetricCloud 0', 'r.VolumetricFog 0', 'r.Water.SingleLayer.Reflection 0', 'r.DistanceFieldShadowing 1', 'grass.sizeScale .33']

    #loop through commands list, entering specified commands/values into in-game console one by one
    for i in commands:
        #open in-game console
        pyautogui.press('`')
        #use pyautogui to type current command into in-game console, interval of 0.05 sec between keystrokes
        pyautogui.write(str(i), interval=0.05)
        #enter command
        pyautogui.press('enter')
        #command completion msg
        print(str(i), "Entered..")

    #Exit msg
    print("All Commands Entered Successfully!")
    print("Enjoy Your Time in the ARK!")
    print('\n')
