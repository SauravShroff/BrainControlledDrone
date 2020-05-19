import os
import numpy as np
import matplotlib.pyplot as plt

trainig_dir = "../model_data/data"
val_dir = "../model_data/validation_data"

def generate_hist(starting_dir):
    times=[]
    ACTIONS = ["left", "right", "none"]
    for action in ACTIONS:
        data_dir = os.path.join(starting_dir,action)
        for item in os.listdir(data_dir):
            times.append(int(item[:10]))
            # times.append((item[:10], action))

    min_time_prenorm = min(times)
    max_time_prenorm = max(times)

    normTimes = [x - min_time_prenorm for x in times]

    min_time_postnorm = min(normTimes)
    max_time_postnorm = max(normTimes)

    times_np = np.array(normTimes)

    # #debug suite
    # print("len is:")
    # print (len(times_np))
    # print("prenorm min:")
    # print (min_time_prenorm)
    # print("prenrom max:")
    # print (max_time_prenorm)
    # print("postnorm min:")
    # print (min_time_postnorm)
    # print("postnorm max:")
    # print (max_time_postnorm)


    range_step = max_time_postnorm / 50
    steps = np.arange(min_time_postnorm, max_time_postnorm, range_step)
    steps = np.append(steps, max_time_postnorm)
    # #debug suite
    # print("steps:")
    # print(steps)
    # print("end bound matches:")
    # print(max(steps) == max_time_postnorm)

    hist,bin_edges = np.histogram(times_np, steps)
    return hist

hist_training = generate_hist(trainig_dir)

print("hist_training:")
print(hist_training)
print(len(hist_training))

hist_val = generate_hist(val_dir)

print("hist_val:")
print(hist_val)
print(len(hist_val))

# print(bin_edges)
# print(len(bin_edges))
# print(bin_edges[:-1])
# print(len(bin_edges[:-1]))
#plt.figure(figsize=[10,8])

# plt.bar(bin_edges[:-1], hist, .8)
# plt.xlim(min(bin_edges), max(bin_edges))
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('Occurance ',fontsize=15)
# plt.ylabel('Frequency',fontsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.ylabel('Frequency',fontsize=15)
# plt.title('Sample Time Dist',fontsize=15)
# plt.show()