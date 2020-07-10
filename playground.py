# import airsim
# import pygame
# import time
# import numpy as np
# from pathlib import Path
# import cyton_interface
# import os
# from pylsl import StreamInlet, resolve_stream

# # a = np.array([])
# # inlet = cyton_interface.connect_to_cyton()
# # a = np.append(a, cyton_interface.pull_fft(inlet))
# # print(a.shape)
# # print(a)

# # first resolve an EEG stream on the lab network
# print("looking for an EEG stream...")
# streams = resolve_stream('type', 'EEG')

# # create a new inlet to read from the stream
# inlet = StreamInlet(streams[0])

# while True:
#     # get a new sample (you can also omit the timestamp part if you're not
#     # interested in it)
#     sample, timestamp = inlet.pull_sample()
#     print(timestamp, sample)


# import airsim
# import pygame
# import time
# import numpy as np
# from pathlib import Path
# import cyton_interface
# import os
# from pylsl import StreamInlet, resolve_stream

# # a = np.array([])
# # inlet = cyton_interface.connect_to_cyton()
# # a = np.append(a, cyton_interface.pull_fft(inlet))
# # print(a.shape)
# # print(a)

# # first resolve an EEG stream on the lab network
# print("looking for an EEG stream...")
# streams = resolve_stream('type', 'EEG')

# # create a new inlet to read from the stream
# inlet = StreamInlet(streams[0])

# sample, timestamp = inlet.pull_sample()
# start = time.time()
# counter = 0
# while True:
#     # get a new sample (you can also omit the timestamp part if you're not
#     # interested in it)
#     sample, timestamp = inlet.pull_sample()
#     if ((time.time() - start) > 2):
#         break
#     counter += 1
# print(counter)

a = "hello"

for i in range(1, len(a), 2):
    print(i)
