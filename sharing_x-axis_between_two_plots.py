import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,6))

ax1 = plt.subplot ()
ax2 = ax1.twinx()
xdata = []
ydata = []
y2 = []
x2 = []

for i in range(20):
    xdata.append(i)
    ydata.append(i)
    if i >9:
        y2.append(i**2)
        x2.append(i)


ax1.plot(xdata,ydata)
ax1.set_xlabel ("Time")
ax1.set_ylabel ("Y")

for tick in ax1.get_yticklabels():
    tick.set_color("blue")

plt.sca(ax2)  #for current working axis

ax2.plot(xdata[10:],y2,c="red")
ax2.set_ylabel(r"$Y_2$")
plt.yticks([0,200,400],["min","mid","max"])


for tick in ax2.get_yticklabels():
    tick.set_color("red")


plt.show()

# ax2.plot(xdata[10:],y2,c="red")
#
#
