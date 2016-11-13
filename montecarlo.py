import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt


#Assignment 1
def gluon_energy():
    return r.random() * .5 + .25
ar = []
for i in range(1000):
    ar += [gluon_energy()]

#plt.hist(ar)
#plt.title("Gluon Energy")
#plt.xlabel("Ratio")
#plt.ylabel("Frequency")

#fig = plt.gcf()

#Assignment 2
def gaussian(n):
    sdev = 2
    return np.exp(-(n**2) / (2 * sdev ** 2)) / (m.sqrt(2 * m.pi * sdev ** 2))

def angle():
    x = r.random()
    y = 10 * r.random() - 5
    if x < gaussian(y):
        return y
    else:
        return False

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
