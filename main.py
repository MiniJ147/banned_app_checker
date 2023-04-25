import psutil
import os
import keyboard
from datetime import datetime
import time

banned_apps = []
running = True

ptr_start = 0

path = input("Enter the txt file of all your banned apps: ")

#getting our pause time so we don't die
print("\nEnter the pause time, in SECONDS, per cycle")
print("This will have a major effect on cpu usage (must be 5 or greater) seconds")
print("The greater the pause time the less cpu power will be used")
print("5 is the lowest amount of pause time")
pause_time = int(input("Enter pause time\n>>> "))

#if they don't set a pause step then we force one so their computer doesnt die
if pause_time < 5:
    pause_time = 5

#reading the file and putting it into a stirng
ban_file = open(path,"r")
banned_apps_string = ban_file.read()
ban_file.close()

#checking if their a \n escape sequence at the end of the file so everything stays constent
if banned_apps_string[len(banned_apps_string)-1]!='\n':
    banned_apps_string+='\n'

#parsing and reading the banned apps file
for ptr_end in range(len(banned_apps_string)):
    if banned_apps_string[ptr_end]=='\n':
        app_name = banned_apps_string[ptr_start: ptr_end]
        ptr_start = ptr_end+1

        banned_apps.append(app_name)

time_start = datetime.now().strftime("%H:%M:%S")
print("Spam W to end Deep Work mode")
print("Start Time: ", time_start)

#life time loop
while running:
    if keyboard.is_pressed('w'):
        running = False
        break
    
    time.sleep(pause_time)

    print("Running Scan [REMINDER]: spam W to exit. If you wish")
    for i in range(len(banned_apps)):
        if banned_apps[i] in (i.name() for i in psutil.process_iter()):
            print("You are supposed to be in deep work rn")
            os.system('taskkill /f /im '+banned_apps[i]) 

#printing final information
print("Deep Work is over")
print("Start Time: ", time_start)
print("End Time: ", datetime.now().strftime("%H:%M:%S"))

input(">>>")
