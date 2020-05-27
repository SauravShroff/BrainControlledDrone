### This file uses pygame to read inputs from the xbox controller
### which acts as our "drone controller" for the purposes of simlation/data collection
### Run with sudo https://www.urbandictionary.com/define.php?term=sudo SUPER USER DO :):):)!!!! (im in a good mood right now)
### Author: Saurav Shroff

import pygame
import numpy as np

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

controller = joysticks[0]
controller.init()
done = False

print(controller.get_numaxes())

while(not done):
    array = np.array([])
    for i in range(controller.get_numaxes()):
        np.append(array, controller.get_axis(i))
    print(array)
