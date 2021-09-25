import matplotlib.pyplot as plt

x = []
y=[]
yTwo = []
for i in range(-100,101,5):
    x.append(i)
    y.append(i)
    yTwo.append(i*2)
print(x,y)
plt.scatter(x,y, s= 15 , c="red")
plt.scatter(x,yTwo, s= 20 , c="green", marker= "*")
plt.show()