### This file is created to collect and store training data according to
### paramaters reading from both the OpenBCI headset and the Spektrum
### controller
### Author: Saurav Shroff
### READ: make sure to locally run "python -m pip install brainflow" otherwise (@NicholasWeaver) "you're GONNA have a BAD DAY"
### Visit: https://brainflow.readthedocs.io/en/stable/UserAPI.html for documentation on the Cyton/Daisy board SDK

import time
import numpy as np
import matplotlib.pyplot as plt

# import brainflow
# from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
# from brainflow.data_filter import DataFilter, FilterTypes, AggOperations

from pylsl import StreamInlet, resolve_stream

# ENABLE_LOGGER = False

# params = BrainFlowInputParams()
# params.serial_port = "serial_port"

# board_id = BoardIds.CYTON_DAISY_BOARD

# board_object = BoardShim (board_id, params)

print("finding stream :)")
streams = resolve_stream('type', 'EEG')
print("resolved stream")
inlet = StreamInlet(streams[0])
print("created inlet")

channel_data = {}

for i in range(5):
    for i in range(16):
        sample, timestep = inlet.pull_sample()
        print("found sample:")
        print(sample)
        print("on timestep:")
        print(timestep)
        if i not in channel_data:
            channel_data[i] = sample
        else:
            channel_data[i].append(sample)
        
for i in channel_data:
    plt.plot(channel_data[i])
plt.show()