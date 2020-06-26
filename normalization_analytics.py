# This programs computs and displays analytics on the distribution that data follows
# in hopes to learn how to best normalize the data
# Author: Saurav Shroff

import os
import random
import time
import numpy as np

start_time = 0
end_time = float('inf')
data_dir = "D:/drone_model_data"
subjects = ["Saurav", "Peter", "Sarah", "Evan"]

sessions = []
for subject in subjects:
    data_dir_local = os.path.join(data_dir, subject)
    for item in os.listdir(data_dir_local):
        item_time = int(item[:10])
        if (item_time >= start_time) and (item_time <= end_time):
            sessions.append(os.path.join(data_dir_local, item))

y_train = None


for session in sessions:
    print("loading from session" + session)
    session_label_data = np.load(os.path.join(session, "2c.npy"))
    if type(y_train) is not np.ndarray:
        y_train = session_label_data
    else:
        y_train = np.concatenate((y_train, session_label_data))

print(y_train.shape)

axis0 = []
axis1 = []
axis2 = []
axis3 = []


for frame in y_train:
    axis0.append(frame[0])
    axis1.append(frame[1])
    axis2.append(frame[2])
    axis3.append(frame[3])
print(axis0)
