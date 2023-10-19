import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 81, 15])
mylabels = (["Apples", "Bananas", "Cherries", "Graphes"])

# # plt.pie(y, labels = mylabels)
# plt.pie(y, labels = mylabels, startangle = 90)

# It will break the pie in single chart
# myexplode = [0.2, 0, 0, 0]

# plt.pie(y, labels = mylabels, explode = myexplode)

#It will say that show the total detail which one is show on table.
plt.pie(y, labels = mylabels)
plt.legend()

plt.show()