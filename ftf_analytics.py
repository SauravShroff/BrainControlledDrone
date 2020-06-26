import numpy as np
from numpy.linalg import norm


relevant_channel = 4
a = np.load("D:/drone_model_data/Saurav/1592253726 to 1592254011/1b.npy")
print(a.shape)

i = 50
current_image = a[i]
current_vector = current_image[relevant_channel]
next_image = a[i+5]
cos_sims = []
for forward_vector in next_image:
    cos_sim = np.dot(forward_vector, current_vector) / \
        (norm(forward_vector)*norm(current_vector))
    cos_sims.append(cos_sim)
print(cos_sims)
