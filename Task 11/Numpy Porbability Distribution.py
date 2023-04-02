import numpy as np
import matplotlib.pyplot as plt

# WE DO NOT CALCULATE PROBABILITY WITH NUMPY
# we draw instead with the help of matplotlib and statistical distribution

arr = np.random.normal(loc=0, scale=1, size=(400, ))
plt.plot(arr)
plt.show()