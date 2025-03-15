import matplotlib.pyplot as plt
import numpy as np

p = np.array([45,20,15,20])

mylab = ["iPhone","Tablets","Laptop","TV"]

myexp = [0,0.2,0,0.2]

mycolors = ["blue","green","yellow","orange"]

plt.pie(p,labels= mylab,startangle= 90, explode= myexp, shadow= True, colors= mycolors)
# plt.pie(p, labels= mylab, startangle= 90, explode= myexp, shadow= True, colors= mycolors)
plt.legend(title = "Device", loc="lower right")
plt.show()