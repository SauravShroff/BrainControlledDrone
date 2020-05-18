import os
import numpy as np
import matplotlib.pyplot as plt

starting_dir = "../model_data/data"

times=[]
ACTIONS = ["left", "right", "none"]
for action in ACTIONS:
    data_dir = os.path.join(starting_dir,action)
    for item in os.listdir(data_dir):
        times.append(int(item[:10]))
        # times.append((item[:10], action))
timesNP = np.array(times)
print (len(timesNP))
hist,bin_edges = np.histogram(timesNP, 10)

plt.figure(figsize=[10,8])

plt.bar(bin_edges[:-1], hist, width = 0.5, color='blue',alpha=0.7)
plt.xlim(min(bin_edges), max(bin_edges))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Sample Time Dist',fontsize=15)
plt.show()