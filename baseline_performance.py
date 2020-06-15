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


y_rand = np.zeros_like(y_train)
