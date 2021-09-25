import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.subplot()
data = []
for i in range(-5,6):
    data.append(i)

# ax.spines["top"].set_color("red")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.yaxis.set_ticks_position("left")
ax.xaxis.set_ticks_position("bottom")

# ax.spines["bottom"].set_position(("axes",0)) #for setting the axes
#
# ax.spines["bottom"].set_position(("outward",0)) #for setting the axes

ax.spines["bottom"].set_position(("data",0)) #for setting the axes

ax.spines["left"].set_position(("data",0)) #for setting the axes



plt.plot(data,data)

plt.show()