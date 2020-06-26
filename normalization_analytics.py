# This programs computs and displays analytics on the distribution that data follows
# in hopes to learn how to best normalize the data
# Author: Saurav Shroff

import os
import random
import time
import numpy as np

data_dir = "D:/drone_model_data"

# first load in all the sessions
sessions = []
for subject in os.listdir(data_dir):
    subject_path = os.path.join(data_dir, subject)
    for session in os.listdir(subject_path):
        session_path = os.path.join(subject_path, session)
        sessions.append(session_path)


vals = None
for session in sessions:
    vals = np.load(session)
