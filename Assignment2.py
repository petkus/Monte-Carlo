import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt

#Assignment 2
def gaussian(n):
    sdev = 2
    return np.exp(-(n**2) / (2 * sdev ** 2)) / (m.sqrt(2 * m.pi * sdev ** 2))

def angle():
    y = r.random()
    x = 10 * r.random() - 5
    if y < gaussian(y):
        return x
    else:
        return False

ar = []
for i in range(1000):
    x = False
    while x == False:
        x = angle()
    ar += [x]

plt.hist(ar, bins=[-1, -.8, -.6, -.4, -.2, 0, .2, .4, .6, .8, 1])
plt.title("Angle")
plt.xlabel("Angle")
plt.ylabel("Frequency")

fig2 = plt.gcf()
plt.show()
