# fill in an accurate file path
import numpy as np

file_path = "D:/model_data/1591659935 to 1591659941/1b.npy"

brain_data_package = np.load(file_path)
print(brain_data_package.shape)
num_frames = brain_data_package.shape[1]

duplicates = 0
for i in range(num_frames - 1):
    if np.array_equal(brain_data_package[0][i], brain_data_package[0][i+1]):
        duplicates += 1

print("Of " + str(num_frames) + " frames, " +
      str(duplicates) + " are duplicates")
