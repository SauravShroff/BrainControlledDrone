# This program trains a classification model for open/closed eyes based on prerecorded training
# data and a specified file location paramater
# Author: Saurav Shroff

import tensorflow as tf
import os
import random
import time
import numpy as np
import helpers.process_array as process
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Reshape
from tensorflow.keras.layers import Conv1D, MaxPooling1D, BatchNormalization

# Define user params
MODEL_NAME = ""

start_time = 0
end_time = 1592702124
data_dir = "D:/eye_model_data"

sessions = []
for item in os.listdir(data_dir):
    item_time = int(item[:10])
    if (item_time >= start_time) and (item_time <= end_time):
        sessions.append(item)

x_train = None
y_train = None

for session in sessions:
    session_data = os.path.join(data_dir, session)
    session_brain_data = np.load(
        os.path.join(session_data, "1b.npy"))
    session_label_data = np.load(
        os.path.join(session_data, "2c.npy"))
    if type(x_train) is not np.ndarray:
        x_train = session_brain_data
        y_train = session_label_data
    else:
        x_train = np.concatenate((x_train, session_brain_data))
        y_train = np.concatenate((y_train, session_label_data))


x_val = x_train[-1000:]
y_val = y_train[-1000:]
x_train = x_train[:-1000]
y_train = y_train[:-1000]

x_train, y_train = process.shuffle_in_unison(x_train, y_train)

print(x_val.shape)
print(y_val.shape)
print(x_train.shape)
print(y_train.shape)

model = Sequential()


model.add(Conv1D(64, (5), padding='same', input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Conv1D(128, (5), padding='same'))
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dense(2))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32,
          epochs=10, validation_data=(x_val, y_val))

model.save("D:/eye_models/" + MODEL_NAME)
