import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Tsig = np.pi/8
Tmu = np.pi / 4
theta = np.random.normal(Tmu, Tsig, 1000)
Z = []
for i in range(1000):
    Z += [.5 * r.random() + .25]


