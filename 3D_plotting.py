import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(5,10))

ax = plt.subplot(211,projection= '3d')
ax2 = plt.subplot(212,projection='3d')

x = []
y = []
z = []

for i in range(20):
    x.append(i%5)
    y.append(i % 10)
    z.append(i)

ax.plot(x,y,z, zdir = 'y' , c ='red')
ax.set_xlim(-4,4)
ax.set_ylim(-5,10)
ax.set_xlim(-5,20)
ax.view_init(30,45)
ax2.scatter(x,y,z,zdir= "z",s=30,c = 'green',depthshade = True,marker='+')
ax2.view_init(45,30)

plt.show()