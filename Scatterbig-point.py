import matplotlib.pyplot as plt
import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))


plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()