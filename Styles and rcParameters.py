import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib

# print(matplotlib.rcParams.keys())
# matplotlib.rcParams ["lines.linewidth"] = 2
# matplotlib.rcParams["lines.color"] = "red"

# print(matplotlib.style.available)
plt.xkcd()
matplotlib.style.use("classic")
xdata = []
ydata = []

for i in range(20):
    xdata.append(i)
    ydata.append(i)

fig = plt.figure(figsize=(6,6))

plt.grid()
plt.plot(xdata,ydata,label = "Plot 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("X and Y axis")
plt.legend(loc = "lower right")
plt.show()