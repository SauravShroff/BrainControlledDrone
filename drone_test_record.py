# This program collects training data for the drone controller regression
# problem. It also simultaneously can load in an existing model and display
# current predicitions. The program records brain data, label values, AND
# predicted label values (run drone_review_session.py to get stats on accuracy
# during a session).
# Author: Saurav Shroff
# Visit: https://brainflow.readthedocs.io/en/stable/UserAPI.html for documentation on the Cyton/Daisy board SDK

import tensorflow as tf
import airsim
import pygame
import time
import numpy as np
from pathlib import Path
import cyton_interface
import os

# Define user params
VIEW_ONLY_MODE = False  # When set to True, data will not be recorded
DISPLAY_MODEL_PREDICTION = True  # Effects on-screen display only
MODEL_NAME = "to_date_6.22.19"
SUBJECT_NAME = "Evan"

# Define some colors
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# Load model for prediction
model = tf.keras.models.load_model("D:/drone_models/" + MODEL_NAME)

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


minX = -0.678
maxX = 0.681

# normalize controller values from range(-0.678, 0.681) to range(0, 1)


def norm(axis):
    return max(0, min(1, (axis - minX) / (maxX - minX)))


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("You are collecting brain -> drone_control data")

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
two_controller = np.array([[0, 0, 0, 0]])
three_simulator = np.array([])
four_guess = np.array([[0, 0, 0, 0]])

# initialize start time
start_time = time.time()
counter = 0

# initialize connection to EEG sensor array
inlet = cyton_interface.connect_to_cyton()


# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP

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
            [[inputs[1], inputs[0], inputs[5], inputs[2]]])

        # take brain image
        brain_data_package = cyton_interface.pull_fft(inlet)
        one_brain.append(brain_data_package)

        # Save label
        two_controller = np.append(two_controller, controller_data_package, 0)

        # This changes the shape from (16, 125) to (1, 16, 125), which is what model() expects
        model_in = np.array([brain_data_package])
        # Generate a guess, and save it to a format that is savable
        guess_package = [[0, 0, 0, 0]]
        # Append guess to the list of all guesses that will be saved
        four_guess = np.append(four_guess, guess_package, 0)
        if DISPLAY_MODEL_PREDICTION:
            textPrint.tprint(screen, "guessing:")
            textPrint.tprint(screen, str(guess_package))

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second.cc
    counter += 1
    clock.tick(60)

###CLOSING AND SAVING SCRIPT###

# GATHER ANALYTICS

end_time = time.time()
seconds_elapsed = end_time - start_time  # time now minus start time
samples_per_second = counter/seconds_elapsed

analytics = np.array(
    [start_time, end_time, seconds_elapsed, samples_per_second])

# PREPEARE ARRAYS FOR SAVING

one_brain = np.array([one_brain])
one_brain = one_brain[0]
one_brain = one_brain[240:-240]  # Remove first and last 10 seconds


two_controller = np.delete(two_controller, 0, 0)  # remove dummy element
for frame in two_controller:
    for val in range(len(frame)):
        frame[val] = norm(frame[val])
two_controller = np.clip(two_controller, 0, 1)
two_controller = two_controller[240:-240]  # Remove first and last 10 seconds

# three_simulator = three_simulator  # edit if needed remove if not

four_guess = four_guess[240:-240]  # Remove first and last 10 seconds

# analytics = analytics  # edit if needed remove if not

# SAVE ARRAYS TO SPECIFIED LOC
if not VIEW_ONLY_MODE:
    folder_name = str(int(start_time)) + " to " + str(int(end_time))
    location = "D:/drone_model_data/" + SUBJECT_NAME + "/" + folder_name
    os.mkdir(location)

    np.save(location + "/1b.npy", one_brain)  # add loc :)
    np.save(location + "/2c.npy", two_controller)
    np.save(location + "/3s.npy", three_simulator)
    np.save(location + "/4g.npy", four_guess)
    np.save(location + "/analytics.npy", analytics)

# close game
pygame.quit()
