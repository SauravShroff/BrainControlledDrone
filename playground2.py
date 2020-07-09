import numpy as np
import helpers.process_array as process
# import tensorflow as tf

array = np.arange(720)
array = np.reshape(array, (8, 9, 10))


array2 = np.arange(720)
array2 = np.reshape(array, (8, 9, 10))

newarray = array[1:3]
# print(newarray)


for i in range(10):
    print(i)
