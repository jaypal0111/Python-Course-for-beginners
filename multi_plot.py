import numpy as np
import matplotlib.pyplot as plt

#plot 1:

x = np.array([0,2,4,6])
y = np.array([4,18,12,16])

plt.subplot(2,4,1)
plt.plot(x,y)

#plot 2:

x = np.array([0,22,4,6])
y = np.array([10,20,30,40])

plt.subplot(2,4,2)
plt.plot(x,y)


# #plot 3:

x = np.array([1,13,5,7])
y = np.array([10,20,30,40])

plt.subplot(2,4,3)
plt.plot(x,y)


# #plot 4:

x = np.array([1,3,15,7])
y = np.array([10,20,30,40])

plt.subplot(2,4,4)
plt.plot(x,y)


# #plot 5:

x = np.array([1,3,5,7])
y = np.array([10,20,30,40])

plt.subplot(2,4,5)
plt.plot(x,y)


#plot 6:

x = np.array([1,3,5,7])
y = np.array([10,20,30,40])

plt.subplot(2,4,6)
plt.plot(x,y)



#plot 7:

x = np.array([1,3,5,7])
y = np.array([10,20,30,40])

plt.subplot(2,4,7)
plt.plot(x,y)



#plot 8:

x = np.array([1,3,5,7])
y = np.array([10,20,30,40])

plt.subplot(2,4,8)
plt.plot(x,y)

plt.suptitle("Multiple Graph")
plt.show()
