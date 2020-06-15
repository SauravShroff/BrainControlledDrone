# This file is created to train a regression model based on prerecorded training
# data and a specified file location paramater
# Author: Saurav Shroff

import tensorflow as tf
import os
import random
import time
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Reshape
from tensorflow.keras.layers import Conv1D, MaxPooling1D, BatchNormalization

start_time = 0
end_time = float('inf')
data_dir = "D:/model_data"

sessions = []
for item in os.listdir(data_dir):
    item_time = int(item[:10])
    if (item_time >= start_time) and (item_time <= end_time):
        sessions.append(item)

x_train = None
y_train = None

for session in sessions:
    session_data = os.path.join(data_dir, session)
    session_brain_data = np.load(os.path.join(session_data, "1b.npy"))
    session_label_data = np.load(os.path.join(session_data, "2c.npy"))
    x_train = session_brain_data
    y_train = session_label_data


x_val = x_train[-1000:]
y_val = y_train[-1000:]
x_train = x_train[:-1000]
y_train = y_train[:-1000]

print(x_val.shape)
print(y_val.shape)
print(x_train.shape)
print(y_train.shape)

model = Sequential()


model.add(Conv1D(64, (5), padding='same', input_shape=(16, 125)))
model.add(Activation('relu'))

model.add(Dense(4))
model.add(Activation('sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='adam', metrics=['mean_squared_error'])
model.fit(x_train, y_train, batch_size=1,
          epochs=10, validation_data=(x_val, y_val))
