import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("Salesa")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("Income")

#plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([10, 50, 90, 70])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("price")

plt.show()