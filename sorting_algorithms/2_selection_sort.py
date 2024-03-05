import matplotlib.pyplot as plt
import numpy as np

amount = 15

lst = np.random.permutation(np.arange(1, amount + 1))
x = np.arange(0, amount, 1)

n = len(lst)

for i in range(n):
    minimum, minIndex = float("inf"), 0
    for j in range(i, n):
        if lst[j] < minimum:
            plt.bar(x, lst)
            plt.pause(0.01)
            plt.clf()
            minimum = lst[j]
            minIndex = j
    lst[i], lst[minIndex] = lst[minIndex], lst[i]
    
plt.bar(x, lst)
plt.pause(0.01)
plt.show(block=False)

plt.waitforbuttonpress()