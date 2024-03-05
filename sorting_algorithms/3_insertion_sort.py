import matplotlib.pyplot as plt
import numpy as np

amount = 15
lst = np.random.permutation(np.arange(1, amount + 1))
x = np.arange(0, amount, 1)

n = len(lst)

for i in range(1, n):
    temp = lst[i]
    j = i - 1
    while j >= 0 and temp < lst[j]:
        plt.bar(x, lst)
        plt.pause(0.01)
        plt.clf()
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = temp

plt.bar(x, lst)
plt.pause(0.01)
plt.show(block=False)

plt.waitforbuttonpress()