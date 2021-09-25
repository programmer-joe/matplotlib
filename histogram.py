import matplotlib.pyplot as plt
from random import gauss

x1 = []
w = []
x2 = []
for i in range(200):
    value = gauss(3,2)
    value2 = gauss(3,2)
    w.append(i)
    if value <= 0:
        x1.append(0)
    elif value <= 1:
        x1.append(1)
    elif value <= 2:
        x1.append(2)
    elif value <= 3:
        x1.append(3)
    elif value <= 4:
        x1.append(4)
    elif value <= 5:
        x1.append(5)
    elif value <= 6:
        x1.append(6)
    else:
        x1.append(7)

    if value2 <= 0:
        x2.append(0)
    elif value2 <= 1:
        x2.append(1)
    elif value2 <= 2:
        x2.append(2)
    elif value2 <= 3:
        x2.append(3)
    elif value2 <= 4:
        x2.append(4)
    elif value2 <= 5:
        x2.append(5)

    elif value2 <= 6:
        x2.append(6)
    else:
        x2.append(7)

#plt.hist(x,bins=range(9),align='left', weights= range(len(x)))
#plt.hist(x,bins=range(9),align='left', weights= w,cumulative= False,orientation='horizontal',rwidth=0.9,label= 'data 1',stacked=True)
plt.hist(x = (x1,x2),bins=range(9),align='left',color=['red',"blue"], weights= [w,w],cumulative= False,
         orientation='horizontal',rwidth=0.9,label= ['data 1','data 2'],stacked=False)
# cumulative for cumulative frequency curve ---- stacked as it sounds
plt.legend()
plt.show()