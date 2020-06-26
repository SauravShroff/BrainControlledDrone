# This file is created to train a regression model based on prerecorded training
# data and a specified file location paramater
# Author: Saurav Shroff

import tensorflow as tf
import os
import random
import time
import numpy as np
import helpers.process_array as process
import baseline_performance
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Reshape
from tensorflow.keras.layers import Conv1D, MaxPooling1D, BatchNormalization

# Define user params
MODEL_NAME = "to_date_6.23.19"
SAVE_MODEL = False

start_time = 0
end_time = float('inf')
data_dir = "D:/drone_model_data"
subjects = ["Saurav", "Peter", "Sarah", "Evan"]
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

# Set aside validation data
x_val = x_train[-1000:]
y_val = y_train[-1000:]
baseline_performance.compute_baseline(y_val)  # Print baseline perf on val
x_train = x_train[: -1000]
y_train = y_train[: -1000]

x_train, y_train = process.shuffle_in_unison(x_train, y_train)

print(x_val.shape)
print(y_val.shape)
print(x_train.shape)
print(y_train.shape)

# Define model
model = Sequential()

model.add(Conv1D(64, (5), padding='same', input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Conv1D(128, (5), padding='same'))
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dense(4))
model.add(Activation('sigmoid'))

# Compile and train
model.compile(loss='mean_squared_error',
              optimizer='adam', metrics=['mean_absolute_error'])
model.fit(x_train, y_train, batch_size=32,
          epochs=10, validation_data=(x_val, y_val))

# Save if the user wanted to save
if SAVE_MODEL:
    model.save("D:/drone_models/" + MODEL_NAME)
    print("saved")
else:
    print("not saved as per user param")
