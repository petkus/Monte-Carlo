import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt

#Assignment 3
def getpoint():
    x = r.random() * 2 - 1
    y = r.random() * 2 - 1
    if(x ** 2 + y ** 2 <= 1):
        return 1
    else:
        return 0

def getpi():
    p = 0
    for x in range(10000):
        p += getpoint()
    return 4 * p / 10000
ar = []
for x in range(10):
    ar += [getpi()]

mean = m.pi
sdev = 1

plt.hist(ar, bins=[mean - 2 * sdev, mean - sdev, mean, mean + sdev, mean + 2 * sdev])
plt.title("Pi")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()
