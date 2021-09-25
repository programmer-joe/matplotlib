import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d
from random import randint

fig = plt.figure(figsize=(8,8))
ax = plt.subplot (111,projection = '3d')

for z in range(5):
    x = []
    y = []
    for second in range(100):
        x.append(second)
        y.append(randint(1,10))

    #ax.bar(x,y,zs = z/2,zdir = 'z')#left, height,zs,zdir
    #ax.bar(x, y, zs=z / 2, zdir='x')  # left, height,zs,zdir
    ax.bar(x, y, zs=z / 2, zdir='y')  # left, height,zs,zdir
ax.set_ylabel ('y')
ax.set_xlabel ('x')
ax.set_zlabel ('z')
ax.set_zlim(0,14)
ax.view_init(20,10)
ax.text(x=4,y =2 ,z=9 , s ="This is our last histogram",
        bbox = dict(facecolor = 'white',alpha = 0.5),color ='red',fontsize = 15)#x,y,z
ax.text(x=4,y =0 ,z=9 , s ="This is our first histogram",
        bbox = dict(facecolor = 'white',alpha = 0.2),color ='grey',fontsize = 15)#x,y,z

plt.show()