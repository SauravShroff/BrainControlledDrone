# fill in an accurate file path
import numpy as np

file_path = "D:/model_data/1591659935 to 1591659941"

brain_data_package = np.load(file_path + "/1b.npy")
print(brain_data_package.shape)
num_frames = brain_data_package.shape[1]

duplicates = 0
for i in range(num_frames - 1):
    if np.array_equal(brain_data_package[0][i], brain_data_package[0][i+1]):
        duplicates += 1

print("Of " + str(num_frames) + " frames, " +
      str(duplicates) + " are duplicates")


analytics = np.load(
    file_path + "/analytics.npy").tolist()
print("the recording started at " + str(analytics[0]) + ", ended at " + str(
    analytics[1]) + ", and lasted " + str(analytics[2]) + " seconds, with an average FPS of " + str(analytics[3]) + ".")