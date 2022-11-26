#!/usr/bin/python3
#Document   : main.py
#Created on : Sat 24 Nov 2022
#Last Update: Sat 25 Nov 2022
#Author     : Top Shelf Technology
#Description: A script to create automated tutorials

import subprocess, time, pyautogui

time.sleep(1)

file = open("script",'r')
line = file.readline()

while line:

    time.sleep(0.2)

    splitl = line.split(chr(124))

    # Speak text
    if splitl[0] == "speak":
        subprocess.run(["espeak", splitl[1]])
    
    # Write text
    elif splitl[0] == "write":
        pyautogui.typewrite("".join(splitl[1:]),interval=0.1)

    # Press a button
    elif splitl[0] == "press":
        print(splitl[1])
        pyautogui.hotkey(splitl[1].strip())

    line = file.readline()

file.close()