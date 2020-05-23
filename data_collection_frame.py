### This file is created to collect and store training data according to
### paramaters reading from both the OpenBCI headset and the Spektrum
### controller
### Author: Saurav Shroff
### READ: make sure to locally run "python -m pip install brainflow" otherwise (@NicholasWeaver) "you're GONNA have a BAD DAY"
### Visit: https://brainflow.readthedocs.io/en/stable/UserAPI.html for documentation on the Cyton/Daisy board SDK

import time
import numpy as np

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations

board_id = BoardIds.CYTON_DAISY_BOARD
