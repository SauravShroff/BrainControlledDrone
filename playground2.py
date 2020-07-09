import numpy as np
import helpers.process_array as process
# import tensorflow as tf
from joblib import dump, load
MODEL_NAME = "hello"
models = load("D:/drone_models/" + MODEL_NAME)
print(models)
