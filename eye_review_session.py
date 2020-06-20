import numpy as np

file_path = "D:/eye_model_data/1592501250 to 1592501687"

true_eye = np.load(file_path + "/2c.npy")
guess_eye = np.load(file_path + "/3g.npy")
print(true_eye.shape)
print(guess_eye.shape)

total_frames = true_eye.shape[0]
correct_frames = 0
for i in range(total_frames):
    if true_eye[i][0] == 1:
        guess = 0
    else:
        guess = 1
    if guess_eye[i][guess] > guess_eye[i][guess-1]:
        correct_frames += 1

print(correct_frames/total_frames)
