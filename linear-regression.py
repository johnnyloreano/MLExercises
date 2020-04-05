import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(1,1,1000)
data2 = 100 + (data + np.random.normal(1,1,1000)) * 3
plt.scatter(data,data2)

plt.show()