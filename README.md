# banned_app_checker
This app will prevent you from opening apps which you have listed as "banned" to prevent you from getting distracted while working.

[PS]:
  I uploaded the source code so you can either run it in command line or build it into your own .exe file. 
  I did not want people to think it was malware so I allowed people to view the code.

[COMMANDS]

Install pyinstaller (only if you do not have it)
  pip install pyinstaller

Build with pyinstaller (this will create an .exe and you have to installer pyinstaller):
  pyinstaller --onefile main.py
  
Run within command line:
  py main.py

[INFOMRATION]

How does this work?

You need to create a .txt file where you can put all your apps which you want banned.
An example can be shown within the repo (banned.txt).

To exit just spam 'w' and it will close out and record the amount of time you were in work for.

[WARNING]
You need to find the specfic .exe file name for it to work. 
EX:
  discord.exe --> will not work
  Discord.exe --> will work as this is what the .exe file is actucally named in your computer
