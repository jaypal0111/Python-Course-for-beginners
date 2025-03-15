# python3 -m pip install -U pip
# python3 -m pip install -U matplotlib

import matplotlib.pyplot as plt
import numpy as np


#x = np.array(["A","B","C","D"])
#y = np.array([2,6,1,12])

x = [10,20,15,21]
y = [10,5,7,23]
# (x,y) = (10,10) (20,5) (15,7) (21,23) 
# plt.bar(x,y)
plt.bar(x,y,color = "green", width= 3)
plt.show()
