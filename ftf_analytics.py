import numpy as np
from numpy.linalg import norm


relevant_channel = 4
a = np.load("D:/model_data/1591659935 to 1591659941/1b.npy")
a = a[0]
print(a.shape)

i = 16
current_image = a[i]
current_vector = current_image[relevant_channel]
next_image = a[i+1]
cos_sims = []
for forward_vector in next_image:
    cos_sim = np.dot(forward_vector, current_vector) / \
        (norm(forward_vector)*norm(current_vector))
    cos_sims.append(cos_sim)
print(cos_sims)
