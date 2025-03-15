#pip install matplotlib

#import  matplotlib
import matplotlib.pyplot as plt

import numpy as np

#print(matplotlib.__version__)

xpoint = np.array([1,8])
# ypoint = np.array([3,10])

# xpoint = np.array([1,2,9,11])
# ypoint = np.array([3,8,4,9,12])
ypoint = np.array([3,8,4,10])
y2point = np.array([6,2,10,11])

# plt.plot(xpoint,ypoint,'o')
# plt.plot(ypoint, marker = 'o')

# plt.plot(ypoint, linestyle = 'dotted', marker = 'o')
# plt.plot(ypoint, linestyle = 'dashed')
# plt.plot(ypoint, linestyle = 'dashed', color = 'r')
# plt.plot(ypoint, linestyle = 'dashed', color = '#4CAF50')
# plt.plot(ypoint, linewidth = 10.0)
# plt.plot(ypoint)
# plt.plot(y2point)
plt.plot(ypoint,y2point)
plt.show()