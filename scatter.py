import numpy as np
import matplotlib.pyplot as plt

x = np.array([5,7,8,9,11,4,2,6,9,2,15,18,29])
y = np.array([55,67,78,70,87,123,93,22,25,26,34,35,36])

colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# colors = np.array(["red","green","blue","black"])


# plt.scatter(x,y, c = colors)


# x = np.array([15,17,18,22])
# y = np.array([55,67,78,11])


# plt.scatter(x,y, color = 'orange')

plt.scatter(x,y, c = colors)

plt.show()