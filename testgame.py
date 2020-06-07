# Hello
import airsim
import pygame
import time
import numpy as np
from pathlib import Path
import cyton_interface

# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')


# connect to the AirSim simulator
# client = airsim.MultirotorClient()
# client.confirmConnection()
# client.enableApiControl(True)
# client.armDisarm(True)


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("We out here making rotis u know how it be")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

# initialize arrays
one_brain = np.array([])
two_controller = np.array([[0, 0, 0, 0, 0]])
three_simulator = np.array([])

# initialize start time
start_time = time.time()
counter = 0
inlet = cyton_interface.connect_to_cyton()


# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user clicked close.
            done = True  # Flag that we are done so we exit this loop.

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        # Order: (0)Rudder (Higher = left), (1)Throttle (Higher = up), (2)L/R Bank (Higher = left), (5)Pitch (Higher = forward)
        inputs = []
        for i in range(axes):
            axis = joystick.get_axis(i)
            inputs.append(axis)
            textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        textPrint.unindent()

        controller_data_package = np.array(
            [[inputs[1], inputs[0], inputs[5], inputs[2], time.time()]])
        brain_data_package = cyton_interface.pull_fft(inlet)
        # print(controller_data_package)
        two_controller = np.append(two_controller, controller_data_package, 0)

        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen,
                             "Button {:>2} value: {}".format(i, button))
        textPrint.unindent()

        textPrint.unindent()

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.cc
    counter += 1
    clock.tick(20)

# Close the window and quit.
# B
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.

# SAURAV ADD CODE TO SAVE FILES HERE PLEASE AND THANKS :)

# remove the first dummy element from the np array
two_controller = np.delete(two_controller, 0, 0)


seconds_elapsed = time.time() - start_time  # cur time minus start time

samples = two_controller.shape[0]
samples_per_second = samples/seconds_elapsed
cycles_per_second = counter/seconds_elapsed
print(samples_per_second)
print(cycles_per_second)
print(two_controller)
pygame.quit()
