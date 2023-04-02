import pandas as pd
import numpy as np
from pandas import Series, DataFrame

obj = pd.Series([4, 7, -5, 3])
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

data = {'state': ['Ohio', 'Ohio', 'Nevada', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2001, 2000, 2005, 2003, 2004, 2002],
        'pop': [1.5, 1.7, 2.6, 3.1, 2.4, 3.9]}
# nested dictionary
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2005: 1.7, 2001: 1.7, 2002: 3.6}}

