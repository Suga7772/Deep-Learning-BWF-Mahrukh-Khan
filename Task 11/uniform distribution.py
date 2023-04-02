import numpy as np
import matplotlib.pyplot as mtl

# equal probability at high and low range
arr = np.random.uniform(-1, 0, 1000)
mtl.hist(arr)
mtl.show()