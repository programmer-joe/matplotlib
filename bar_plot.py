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
plt.bar(index,group1,width = 0.5,color = ['grey','blue','green'], edgecolor = 'blue', linewidth = 2, yerr =group1err,tick_label=ident )
plt.bar(index,group2, width = 0.5 , align = 'center',bottom=group1,edgecolor ='black',linewidth =2 , yerr = group1,ecolor ='black')
plt.show()