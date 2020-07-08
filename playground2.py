import numpy as np
import helpers.process_array as process
# import tensorflow as tf

array = np.arange(18)
array = np.reshape(array, (9, 2))
print(array)
array = array.transpose()
print(array)
