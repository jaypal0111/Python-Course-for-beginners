import matplotlib.pyplot as plt
import numpy as np

h = np.random.normal(186,5,255)

# 1st para for count of generating rand numbers
#2nd  para difference for generating rand numbers
# 3rd up to generate max till that perticular number
# h = np.random.normal(10,2,20)

plt.hist(h,color = "green",orientation='vertical',histtype='bar')



print(h)

plt.show()
