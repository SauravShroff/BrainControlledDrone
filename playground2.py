import numpy as np
import helpers.process_array as process
# import tensorflow as tf
from joblib import dump, load

classifiers = load("D:\drone_models\svc_single_frame_7.9.2020")
for classifier in classifiers:
    print(classifier)
