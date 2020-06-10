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


model = Sequential()

model.add(Conv1D(64, (5), padding='same', input_shape=train_X.shape[1:]))
model.add(Activation('relu'))
model.add(Dropout(0.2))


model.compile(loss='mean_squared_error',
              optimizer='adam', metrics=['mean_squared_error'])
