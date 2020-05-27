### This file uses pygame to read inputs from the xbox controller
### which acts as our "drone controller" for the purposes of simlation/data collection
### Run with sudo https://www.urbandictionary.com/define.php?term=sudo SUPER USER DO :):):)!!!! (im in a good mood right now)
### Author: Saurav Shroff

import pygame

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

controller = joysticks[0]
controller.init()
done = False


while(not done):
    outputStr = ""
    for i in range(controller.get_numaxes()):
        outputStr += str(controller.get_axis(i)) + " "
    print(f'{outputStr}\r', end="")
