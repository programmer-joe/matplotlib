import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin

fig = plt.figure(figsize = (5,6))
ax = plt.subplot(111,projection='3d')

x = []
y = []
z = []

for i in range(100):
    temp = []
    tempz = []

    for j in range(100):
        temp.append(j/10)
        tempz.append(i/10)

    x.append(temp)
    y.append(temp)
    z.append(tempz)

ax.plot_surface(x,y,z)
ax.view_init(45,60)
plt.show()