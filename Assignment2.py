import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt

#Assignment 2
def gaussian(n):
    mean = m.pi / 4
    sdev = mean / 2
    return np.exp(-((n - mean)**2) / (2 * sdev ** 2)) / (m.sqrt(2 * m.pi * sdev ** 2))

def angle():
    y = r.random()
    x = m.pi / 2 * r.random()
    if y < gaussian(x):
        return x
    else:
        return False

ar = []
for i in range(100000):
    x = False
    while x == False:
        x = angle()
    ar += [x]

mean = m.pi / 4
sdev = mean / 2
plt.hist(ar, bins=[mean - 2 * sdev, mean - sdev, mean, mean + sdev, mean + 2 * sdev])
plt.title("Angle")
plt.xlabel("Angle")
plt.ylabel("Frequency")

plt.show()
