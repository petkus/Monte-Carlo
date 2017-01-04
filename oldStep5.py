import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Assignment 4
#Plotting Z
def gluon_energy():
    return r.random() * .5 + .25
arZ = []
for i in range(1000):
    arZ += [gluon_energy()]
binsZ = np.linspace(.25, .75, num=10)

plt.hist(arZ, binsZ, alpha = .5, label = 'Z')

#Plotting Theta
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

arT = []
for i in range(1000):
    x = False
    while x == False:
        x = angle()
    arT += [x]

mean = m.pi / 4
sdev = mean / 2
binsT = np.linspace(mean - 3*sdev, mean + 3*sdev, num=10)
plt.hist(arT, binsT, alpha = .5, label = 'Theta')
plt.legend(loc='upper right')

#3d Histogram:
#I copied some code from MatPlot lib website, but not too familiar on the
#motivations behind some of it
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(arT, arZ, bins=4, range=[[0, 4], [0, 4]])

xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

plt.show()
