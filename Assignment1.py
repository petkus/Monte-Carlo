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

plt.hist(ar)
plt.title("Gluon Energy")
plt.xlabel("Ratio")
plt.ylabel("Frequency")

fig = plt.gcf()

