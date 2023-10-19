import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 40, 95, 100, 105, 110, 115, 120, 125])
y = np.array([200, 240, 245, 250, 305, 310, 315, 320, 325])

plt.title("sports watch date")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()