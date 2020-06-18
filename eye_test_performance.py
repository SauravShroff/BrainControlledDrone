# Hello
import tensorflow as tf
import airsim
import pygame
import time
import numpy as np
from pathlib import Path
import cyton_interface
import os

# Define user params

SAVE_MODEL_PREDICTION = True
DISPLAY_MODEL_PREDICTION = True

# Define some colors
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)


# Load model for prediction
model = tf.keras.models.load_model("D:/eye_models/new_model")

# Define print class


class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString, color=BLACK):
        textBitmap = self.font.render(textString, True, color)
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

pygame.display.set_caption("You are collecting brain -> eye data")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

# initialize arrays
one_brain = []
two_controller = np.array([[0, 0]])
three_guess = np.array([[0, 0]])


# initialize start time
start_time = time.time()
counter = 0

# initialize connection to EEG sensor array
inlet = cyton_interface.connect_to_cyton()


# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP

    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user clicked close / program was ended from command line
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

        threshold = 0.0

        if inputs[1] > threshold:
            controller_data_package = np.array(
                [[1, 0]])  # open
            textPrint.tprint(screen, "RECORDING OPEN", BLUE)
        else:
            controller_data_package = np.array(
                [[0, 1]])  # close
            textPrint.tprint(screen, "RECORDING CLOSE", BLUE)

        # take brain image
        brain_data_package = cyton_interface.pull_fft(inlet)
        one_brain.append(brain_data_package)

        # print(controller_data_package)
        two_controller = np.append(two_controller, controller_data_package, 0)

        model_in = np.array([brain_data_package])
        guess_package = model(model_in).numpy()
        three_guess = np.append(three_guess, guess_package, 0)
        if DISPLAY_MODEL_PREDICTION:
            if guess_package[0][0] > 0.5:
                textPrint.tprint(screen, "GUESSING OPEN", GREEN)
            else:
                textPrint.tprint(screen, "GUESSING CLOSE", RED)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    counter += 1
    clock.tick(60)

###CLOSING AND SAVING SCRIPT###

# GATHER ANALYTICS

end_time = time.time()
seconds_elapsed = end_time - start_time  # time now minus start time
samples_per_second = counter/seconds_elapsed

analytics = np.array(
    [start_time, end_time, seconds_elapsed, samples_per_second])

# CREATE DIRECTORY FOR SAVING

folder_name = str(int(start_time)) + " to " + str(int(end_time))
location = "D:/eye_model_data/" + folder_name
os.mkdir(location)


# PREPEARE ARRAYS FOR SAVING

one_brain = np.array([one_brain])
one_brain = one_brain[0]

two_controller = np.delete(two_controller, 0, 0)  # remove dummy element

three_guess = np.delete(three_guess, 0, 0)  # remove dummy element

analytics = analytics  # edit if needed remove if not

# SAVE ARRAYS TO SPECIFIED LOC

np.save(location + "/1b.npy", one_brain)
np.save(location + "/2c.npy", two_controller)
if SAVE_MODEL_PREDICTION:
    np.save(location + "/3g.npy", three_guess)
np.save(location + "/analytics.npy", analytics)

# close game
pygame.quit()
