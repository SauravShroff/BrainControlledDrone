# This file is created to train an SVC classification model based on prerecorded training
# data and a specified file location paramater
# Author: Saurav Shroff

import os
import random
import time
import numpy as np
import helpers.process_array as process
import baseline_performance
from sklearn import svm
from joblib import dump, load

# Define user params
MODEL_NAME = "svc_single_frame_7.9.2020"
SAVE_MODEL = False

start_time = 0
end_time = float('inf')
data_dir = "D:/drone_model_data"
subjects = ["Peter", "Evan", "Sarah", "Saurav"]
# First find all the sessions we want to train on
sessions = []
for subject in subjects:
    data_dir_local = os.path.join(data_dir, subject)
    for item in os.listdir(data_dir_local):
        item_time = int(item[:10])
        if (item_time >= start_time) and (item_time <= end_time):
            sessions.append(os.path.join(data_dir_local, item))

x_train = None
y_train = None

# Next load in all the data from each session
for session in sessions:
    print("loading from session" + session)
    session_brain_data = np.load(os.path.join(session, "1b.npy"))
    session_label_data = np.load(os.path.join(session, "2c.npy"))
    if type(x_train) is not np.ndarray:
        x_train = session_brain_data
        y_train = session_label_data
    else:
        x_train = np.concatenate((x_train, session_brain_data))
        y_train = np.concatenate((y_train, session_label_data))

# reshape x_train such that each frame
x_train = x_train.flatten()
x_train = x_train.reshape(-1, 2000)

# Set aside validation data
x_val = x_train[-1000:]
y_val = y_train[-1000:]
print("Val baseline:")
baseline_performance.compute_baseline(y_val)  # Print baseline perf on val
x_train = x_train[: -1000]
y_train = y_train[: -1000]
print("Train baseline:")
baseline_performance.compute_baseline(y_train)

# Randomize the order of training data
x_train, y_train = process.shuffle_in_unison(x_train, y_train)

# Convert y_train labels from a list of N 4-length arrays, to 4 lists of N items
y_train = y_train.transpose()
y_val = y_val.transpose()

# Convert train and val labels to one hot vectors
for axis in y_train:
    for i in range(len(axis)):
        if axis[i] > 0.5:
            axis[i] = 1
        else:
            axis[i] = 0

print(x_val.shape)
print(y_val.shape)
print(x_train.shape)
print(y_train.shape)

# Define models (one for each controller axis)
models = [svm.LinearSVC(dual=False), svm.LinearSVC(
    dual=False), svm.LinearSVC(dual=False), svm.LinearSVC(dual=False)]

# Compile and train
for i in range(len(models)):
    print("training for axis " + str(i))
    models[i].fit(x_train, y_train[i])

# Save if the user wanted to save
if SAVE_MODEL:
    dump(models, "D:/drone_models/" + MODEL_NAME)
else:
    print("not saved as per user param")
