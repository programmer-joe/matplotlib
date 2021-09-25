import matplotlib.pyplot as plt

x =[]
y = []

xAxisTicks = ['min','max','mode']

for i in range(0,101,5):
    x.append(i)
    y.append(i)

plt.plot(x,y,label ='graph 1',ls= '--',marker = 'o',mfc ='blue')
plt.title("This is a test")
plt.xlabel("X-axis" )
plt.ylabel("Y-axis")
plt.legend(loc = 'lower right')
plt.xticks([0,50,100],xAxisTicks,rotation = 90)
plt.show()