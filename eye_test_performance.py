import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("D:/eye_models/new_model")

a = np.zeros((1, 16, 125))


print(model.__call__(a))
