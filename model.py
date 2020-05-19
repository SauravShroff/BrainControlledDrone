import tensorflow as tf
import os
import random
import time
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Reshape
from tensorflow.keras.layers import Conv1D, MaxPooling1D, BatchNormalization


#file drop
# set_count = 20000
# training_vals = np.array([])
# for i in range(set_count):
#     a = np.load('../model_data/data/left/1572814932.npy')
#     np.append(training_vals, a)
#     x = "load no error num: " + str((i + 1))
#     print('{}\r'.format(x), end="")

ACTIONS = ["left", "right", "none"]
reshape = (-1, 16, 60)


def create_data(starting_dir="../model_data/data"):
    files_loaded = 0
    training_data = {}
    for action in ACTIONS:
        if action not in training_data:
            training_data[action] = []

        data_dir = os.path.join(starting_dir,action)
        for item in os.listdir(data_dir):
          x = "Loaded " + str((files_loaded + 1)) + " files from within " + starting_dir
          files_loaded += 1
          print('{}\r'.format(x), end="")
          data = np.load(os.path.join(data_dir, item))
          for item in data:
              training_data[action].append(item)

    lengths = [len(training_data[action]) for action in ACTIONS]
    print(lengths)

    for action in ACTIONS:
        np.random.shuffle(training_data[action])  # note that regular shuffle is GOOF af
        training_data[action] = training_data[action][:min(lengths)]

    lengths = [len(training_data[action]) for action in ACTIONS]
    print(lengths)
    # creating X, y 
    combined_data = []
    for action in ACTIONS:
        for data in training_data[action]:

            if action == "left":
                combined_data.append([data, [1, 0, 0]])

            elif action == "right":

                combined_data.append([data, [0, 0, 1]])

            elif action == "none":
                combined_data.append([data, [0, 1, 0]])

    np.random.shuffle(combined_data)
    print("length:",len(combined_data))
    return combined_data


print("creating training data")
traindata = create_data()

train_X = []
train_y = []
for X, y in traindata:
    train_X.append(X)
    train_y.append(y)
print("train samples length:")
print(len(train_X))
print("train labels length:")
print(len(train_y))


print("creating validation data")
testdata = create_data(starting_dir="../model_data/validation_data")
test_X = []
test_y = []
for X, y in testdata:
    test_X.append(X)
    test_y.append(y)
print("val samples length:")
print(len(test_X))
print("val labels length:")
print(len(test_y))

train_X = np.clip(np.array(train_X).reshape(reshape) - np.mean(train_X), -10, 10) / 10
test_X = np.clip(np.array(test_X).reshape(reshape) - np.mean(test_X), -10, 10) / 10

train_y = np.array(train_y)
test_y = np.array(test_y)

model = Sequential()

model.add(Conv1D(64, (5), padding='same', input_shape=train_X.shape[1:]))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Conv1D(128, (5), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.2))

# model.add(Conv1D(256, (5), padding='same'))
# model.add(Activation('relu'))
# model.add(Dropout(0.2))

# model.add(Conv1D(512, (5), padding='same'))
# model.add(Activation('relu'))
# model.add(Dropout(0.2))

model.add(Conv1D(3, (16)))
model.add(Reshape((3,)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs = 10
batch_size = 32
#print("executing training iteration " + str(itteration))
model.fit(train_X, train_y, batch_size=batch_size, epochs=epochs, validation_data=(test_X, test_y))
#model_name = f"new_models/{round(score[1]*100,2)}-acc-64x3-batch-norm-{epoch}epoch-{int(time.time())}-loss-{round(score[0],2)}.model"
#model.save(model_name)
#print("saved:")
#print(MODEL_NAME)