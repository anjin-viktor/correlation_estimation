# -*- coding: cp1251 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys
import csv

if len(sys.argv) != 3:
    print("`correlations.csv` and `correlations_wo_embedding.csv` arguments expected")
    exit(1)

y1 = []
y2 = []

x = []

n_bins = 2500

xmin = 0
xmax = 0.01

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        y1.append(float(row[1]))

with open(sys.argv[2]) as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        y2.append(float(row[1]))

y2 = np.array(y2)
y1 = np.array(y1)

fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)
plt.yscale('log')

min = 0
max = 0

for y in y1:
    if y > max:
        max = y
    if y < min:
        min = y
for y in y2:
    if y > max:
        max = y
    if y < min:
        min = y

#print("min: %d max: %d" % (min, max))
#min = 0
max = 0.000003
##borders for better drawing
#bins = np.linspace(-200, 6000, n_bins)
#axs.set(xlim=(-200, 6000))
bins = np.linspace(min, max, n_bins)
axs.set(xlim=(min, max))


axs.hist(y1, bins=bins, label='With Embedding')
axs.hist(y2, bins=bins, label='Without Embedding')

plt.title('Without filtering')
#plt.title('DCT-based filtering with dctdnoiz')
plt.xlabel('Correlation Value')
plt.ylabel('Number of Images')
plt.legend()

#plt.axvline(np.mean(y1), color='blue', linestyle='dashed', linewidth=1)
#plt.text(np.mean(y1), plt.ylim()[1]*0.9, 'Mean', color='blue')

#plt.axvline(np.mean(y2), color='orange', linestyle='dashed', linewidth=1)
#plt.text(np.mean(y2), plt.ylim()[1]*0.9, 'Mean', color='orange')


mean_y1 = np.mean(y1)
mean_y2 = np.mean(y2)

# Add dashed mean line for y1 (With Embedding)
axs.axvline(mean_y1, color='blue', linestyle='dashed', linewidth=1)
axs.text(mean_y1 + 50, axs.get_ylim()[1]*0.6, f'Mean = {mean_y1:.1f}', color='blue', ha='left', fontsize=9)

# Add dashed mean line for y2 (Without Embedding)
axs.axvline(mean_y2, color='orange', linestyle='dashed', linewidth=1)
axs.text(mean_y2 + 50, axs.get_ylim()[1]*0.6, f'Mean = {mean_y2:.3f}', color='orange', ha='left', fontsize=9)


plt.show()
