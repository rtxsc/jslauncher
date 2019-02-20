#!/usr/bin/python
# this code will be run by launcher.py
from time import sleep
import sys
import os
import pygame
import subprocess

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_ Python Script Codeone  -_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


buttonHome = 8

os.environ["SDL_VIDEODRIVER"] = "dummy" # Removes the need to have a GUI window
os.putenv('DISPLAY',':0')
pygame.init()
print ('Codeone Finding Joystick')              
while True:
    try:
        try:
            pygame.joystick.init() 
            # Attempt to setup the joystick
            if pygame.joystick.get_count() < 1:
                # No joystick attached, toggle the LED
                pygame.joystick.quit()
                sleep(0.1)
            else:
                # We have a joystick, attempt to initialise it!
                joystick = pygame.joystick.Joystick(0)
                break
        except pygame.error:
            # Failed to connect to the joystick, toggle the LED
            pygame.joystick.quit()
            sleep(0.1)
    except KeyboardInterrupt:
        # CTRL+C exit, give up
        print ('\nCodeone: user aborted')              
        sys.exit()
print ('Codeone: joystick found! hoorayy')              
joystick.init()
try:
    a = 0
    while 1:
        start = 0
        home = 0
        # Get the latest events from the system
        hadEvent = False
        events = pygame.event.get()
        # Handle each event individually
        for event in events:
            if event.type == pygame.QUIT:
            # User exit
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
            # A button on the joystick just got pushed down
                hadEvent = True                    
            if hadEvent:
                if joystick.get_button(buttonHome):
                    home = 1
                if home:
                    raise KeyboardInterrupt
            print("codeone event:{}".format(event.type))
            
        a += 1
        print("a : {}".format(a))
        sleep(0.1)
        if joystick.get_button(buttonHome):
            raise KeyboardInterrupt
except KeyboardInterrupt:
    print("bye2 from codeone")
