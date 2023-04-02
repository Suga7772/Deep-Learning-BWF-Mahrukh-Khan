import numpy as np
import matplotlib.pyplot as plt

#   WEIBULL Distritbution

shape = 5  # how quickly a component is likly to fail, steepness
arr = np.random.weibull(shape, 400)
plt.hist(arr)
plt.show()