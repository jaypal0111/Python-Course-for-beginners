import numpy as np
import matplotlib.pyplot as plt


x = np.array([75,80,85,90,95,100,105,110,115,120,125])
y = np.array([200,210,220,230,240,250,260,270,275,280,285])


font1 = {'family' : 'arial','color':'blue','size':22,'weight':'bold'}
font2 = {'family' : 'arial','color':'red','size':18,'weight':'bold'}



plt.plot(x, y,color = 'blue', linestyle = 'dotted',marker = 'o')

plt.title("Sport Analysis", fontdict= font1, loc = 'left',style='italic')
plt.xlabel("Average run", fontdict=font2)
plt.ylabel("Number of Balls", fontdict=font2)

# to get grid view
# plt.grid()

# plt.grid(axis = 'x')
# plt.grid(axis = 'y')

plt.grid(color = 'red', linestyle = 'dotted', linewidth = 0.3)
plt.show()