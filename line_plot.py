import matplotlib.pyplot as plt

x = []
y=[]
yTwo = []

xAxisTicks = ["min","mid","max"]
yAxisTicks = ["Morning","lunch","afternoon","dinner","Evening",'night']
#plt.figure(figsize=(10,8))
for i in range(-100,101,5):
    x.append(i)
    y.append(i)
    yTwo.append(i*2)
#print(x,y)

plt.plot(x,y, c="red",ls="--", lw = 10,marker = "o",ms = 20,fillstyle = "left",mfc = "blue",label = "graph1")
plt.plot(x,yTwo,c = "green",label ="graph2")

plt.xlabel("This is the x-axis",color = "red",fontsize = 10,horizontalalignment ="left",verticalalignment = "top")
plt.ylabel("This is the y-axis",color = "red",fontsize = 10,horizontalalignment ="left",verticalalignment = "top")
plt.title(r"This is our title $\frac{1}{2}$",color = "blue",fontsize = 25)

plt.legend(loc = "lower right")
plt.text(0,125,"This is a text",color ='yellow',rotation =0,style ='italic',fontsize = 15 ,weight ='heavy',
         bbox = dict(facecolor = 'blue',alpha = 0.3))

#plt.xticks([-100,0,100],xAxisTicks, rotation = 90)
#plt.yticks([-200,-100,0,100,150,200],yAxisTicks,rotation = 45)

plt.annotate(xy = (0,20), xytext = (-25,150),text = 'annotation',arrowprops = dict(width = 5, headlength=10,headwidth = 10,
                                                                                shrink=0.0,facecolor="red"),
                                                                                horizontalalignment="right",verticalalignment="top")
#
# plt.savefig("firstpic.pdf",facecolor='orange',orientation = 'landscape',transparent = True)
#plt.xscale('log',basex= 6,subsx = [1,2,3,4,5,6])
plt.xscale('symlog',base= 10,subs = [1,2,3,4,5,6],linthresh = 10,linscale = 2)
#plt.yscale('symlog',base= 10,subs = [1,2,3,4,5,6],linthresh = 10,linscale = 2)

plt.show()