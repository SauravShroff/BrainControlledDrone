import os
import random
import time
import numpy as np


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
    session_label_data = np.load(os.path.join(session_data, "2c.npy"))
    y_train = session_label_data

shape = y_train.shape
y_rand = np.random.rand(shape[0], shape[1])


count = 0
sum_vals = 0
total_val = 0
for frame in range(len(y_rand)):
    for stick in range(len(y_rand[0])):
        count += 1
        sum_vals += abs(y_train[frame][stick] - y_rand[frame][stick])


print("mean absolute error for random guesses would be:")
print(sum_vals / count)

average = total_val / count
print(average)
