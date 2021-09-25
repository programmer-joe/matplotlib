# creating multiple axis
# import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid1 import Divider
# import mpl_toolkits.axes_grid1.axes_size as Size
# fig = plt.figure(figsize=(8,8))
#
# ax = []
#
# rect = [0.1,0.1,0.5,0.5] # left bottom width height
# for i in range(4):
#     ax.append(fig.add_axes(rect,label = str(i)))
# # ax1 = fig.add_axes(rect, label= "0")
# # ax2 = fig.add_axes(rect, label= "1", sharey = ax1)
# # ax3 = fig.add_axes(rect, label= "2", sharex = ax1)
# # ax4 = fig.add_axes(rect, label= "", sharex = ax1)
#
#
# horiz = [Size.AxesX(ax[0]),Size.Fixed(0.5),Size.AxesX(ax[1])]
# vert = [Size.AxesY(ax[0]),Size.Fixed(0.5),Size.AxesY(ax[2])]
# divider = Divider(fig,rect,horiz,vert) #fig,pos,horizontal
#
# ax[0].set_axes_locator(divider.new_locator(nx= 0,ny =0))
# ax[1].set_axes_locator(divider.new_locator(nx= 2,ny =0))
# ax[2].set_axes_locator(divider.new_locator(nx= 0,ny =2))
# ax[3].set_axes_locator(divider.new_locator(nx= 2,ny =2))
#
# ax[0].set_xlim(0,2)
# ax[1].set_xlim(0,1)
# ax[0].set_ylim(0,1)
# ax[2].set_ylim(0,2)
#
# plt.draw()
# plt.show()

# plotting on multiple axis
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider
import mpl_toolkits.axes_grid1.axes_size as Size
from random import randint
fig = plt.figure(figsize=(8,8))


rect = [0.1,0.1,0.5,0.5] # left bottom width height
ax1 = fig.add_axes(rect, label= "0")
ax2 = fig.add_axes(rect, label= "1", sharey = ax1)
ax3 = fig.add_axes(rect, label= "2", sharex = ax1)
ax4 = fig.add_axes(rect, label= "3")
#ax4 = fig.add_axes(rect, label= "3", sharey = ax3,sharex = ax2) #to make the scatter plot better stop sharing the axis

ax = [ax1,ax2,ax3,ax4]

horiz = [Size.AxesX(ax[0]),Size.Fixed(0.4),Size.AxesX(ax[0])]
vert = [Size.AxesY(ax[0]),Size.Fixed(0.4),Size.AxesY(ax[0])]
divider = Divider(fig,rect,horiz,vert) #fig,pos,horizontal

ax[0].set_axes_locator(divider.new_locator(nx= 0,ny =0))
ax[1].set_axes_locator(divider.new_locator(nx= 2,ny =0))
ax[2].set_axes_locator(divider.new_locator(nx= 0,ny =2))
ax[3].set_axes_locator(divider.new_locator(nx= 2,ny =2))


x = []
y = []
for i in range(1000):
    x.append(randint(0,8))
    y.append(randint(0, 7))

plt.sca(ax1)
plt.hist2d(x,y,bins=[range(10),range(9)])
# plt.colorbar()
ax3.hist(x,bins= range(10))
ax2.hist(y,bins=range(9),orientation = "horizontal")


ax4.scatter (x,y) #to make the scatter plot better stop sharing the axis
cbax = fig.add_axes([0.3,0.1,0.03,0.35])
plt.colorbar(cax=cbax)
ax2.yaxis.set_ticks_position("right")
# ax[0].set_xlim(0,2)
# ax[1].set_xlim(0,1)
# ax[0].set_ylim(0,1)
# ax[2].set_ylim(0,2)

plt.draw()
plt.show()
