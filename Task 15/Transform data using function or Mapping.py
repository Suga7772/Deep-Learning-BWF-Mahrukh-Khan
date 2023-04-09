import pandas as pd
import numpy as np
from numpy import nan as NA

datahh = pd.DataFrame({'food': ['bacon', 'hunter beef', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'jerky'],
'ounces': [4.1, 13, 12, 6, 7.5, 81, 39, 55, 46]})

print(datahh, "\n\n")

meat_to_animal = { 'bacon': 'pig',
                   'hunter beef': 'bull',
                   'pastrami': 'cow',
                   'corned beef': 'cow',
                   'honey ham': 'pig',
                   'jerky': 'cow'
                    }

# mapping accepts function or dict like

lowcase = datahh['food'].str.lower()
print(lowcase, "\n\n")

datahh['animal'] = lowcase.map(meat_to_animal)
print(datahh, "\n\n")

# also could've done using function and lambda function
# data['food'].map(lambda x: meat_to_animal[x.lower()]


