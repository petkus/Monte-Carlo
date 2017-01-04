import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt

#Assignment 3
def getpoint():
    x = r.random() * 2 - 1
    y = r.random() * 2 - 1
    if(x ** 2 + y ** 2 <= 1):
        return 1.0
    else:
        return 0

def getpi():
    p = 0
    num = 10000
    for x in range(num):
        p += getpoint()
    return 4 * p / num
ar = []
for x in range(100):
    ar += [getpi()]

mean = sum(ar) / float(len(ar))
sdev = np.std(ar)

plt.hist(ar, bins=[mean - 3 * sdev, mean - 2 * sdev, mean - sdev, mean, mean +
    sdev, mean + 2 * sdev, mean + 3 * sdev])
plt.title("Pi")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()
