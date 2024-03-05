import matplotlib.pyplot as plt
import numpy as np

amount = 15

lst = np.random.permutation(np.arange(1, amount + 1))
x = np.arange(0, amount, 1)

n = len(lst)

for i in range(n):
    for j in range(0, n - 1 - i):
        plt.bar(x, lst)
        plt.pause(0.01)
        plt.clf()
        
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

plt.bar(x, lst)
plt.pause(0.01) 
plt.show(block=False)


plt.waitforbuttonpress()