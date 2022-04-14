import os
import time
console = str(input("Command: "))
if console == "adventure":
    os.system("python ../src/adventure.py")
        
elif console == "shooter":
    os.system("python ../src/shoot.py")

elif console == "song":
    os.system("python ../src/song.py")
if console == "help":
    print('''
Hello my self Umesh i made this project.
I am not sure this will fit the theme or not
but i gave a try.
You can make everyday less ordinary by making a time table for your day
and use this project every time your bored  by taking a break for few minutes.
Commands
1.help - To see the commands and few information about the project
2.adventure - To play adventure game
3.shooter - To play shooter game
4.song - to play song game
Thank You!
''')
time.sleep(15)
