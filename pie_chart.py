import matplotlib.pyplot as plt
from random import randint

group1 = []
group2 = []
index = []
group1err = []
ident = ['val1','val2','val3','val4','val5']
for i in range (5):

    group1.append(randint(30,40))
    group2.append(randint(30, 40))
    index.append(i)
    group1err.append(randint(1,5))

plt.pie(group1,labels=ident,explode =[0.1,0,0,0,0],colors = ['red','green','black','grey','purple'],
        labeldistance= 1.1, shadow=True,startangle= 0,frame=True,radius=0.4,center=(0.5,0.5))

plt.show()