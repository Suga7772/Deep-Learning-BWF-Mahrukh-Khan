import numpy as np
import matplotlib.pyplot as mtl

arr = np.random.poisson(2, 400)
mtl.plot(arr)
mtl.show()
