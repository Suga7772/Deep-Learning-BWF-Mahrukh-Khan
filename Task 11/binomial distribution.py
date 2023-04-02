import numpy as np
import matplotlib.pyplot as mtl

ar = np.random.binomial(36, 1/6, 400)
mtl.hist(ar)
mtl.show()