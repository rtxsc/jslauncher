#!/usr/bin/env python
# codetwo
from time import sleep
import sys
import os
import pygame
import subprocess

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_ Python Script Codetwo  -_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

buttonHome = 8

os.environ["SDL_VIDEODRIVER"] = "dummy" # Removes the need to have a GUI window
os.putenv('DISPLAY',':0')
pygame.init()
print ('Codetwo Finding Joystick')              
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
        print ('\nCodetwo: user aborted')              
        sys.exit()
print ('Codetwo: joystick found! hoorayy')              
joystick.init()
try:
    b = 0
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
            print("Codetwo event:{}".format(event))
            
        b += 2
        print("b : {}".format(b))
        sleep(0.1)
        if joystick.get_button(buttonHome):
            raise KeyboardInterrupt
except KeyboardInterrupt:
    print("bye2 from Codetwo")
