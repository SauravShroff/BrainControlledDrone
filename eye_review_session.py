import tensorflow as tf
import numpy as np

# Define user params
FILE_PATH = "D:/eye_model_data/1592702292 to 1592702359"
REGENERATE_GUESS = True
MODEL_NAME = "Sarah_Only"
DELETE_CHANGES = False

# labels
true_eye = np.load(FILE_PATH + "/2c.npy")

# either make new guesses based on brain data using a model speicified in MODEL_NAME
# or pull guesses that were made at record-time
if REGENERATE_GUESS:
    model = tf.keras.models.load_model("D:/eye_models/" + MODEL_NAME)
    guess_eye = model(np.load(FILE_PATH + "/1b.npy"))
else:
    guess_eye = np.load(FILE_PATH + "/3g.npy")

# make sure the true values and precicted values are of the same shape
assert(true_eye.shape == guess_eye.shape)

# compute accuracy
total_frames = true_eye.shape[0]
correct_frames = 0
for i in range(total_frames):
    if true_eye[i][0] == 1:
        guess = 0
    else:
        guess = 1
    if guess_eye[i][guess] > guess_eye[i][guess-1]:
        correct_frames += 1

print(correct_frames/total_frames)
