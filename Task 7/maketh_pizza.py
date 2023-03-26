from pizza import make_pizza as mp
# function make pizza can be called by mk only
mp(20, 'thin crust', 'margarita', 'neopolitan')
mp(7, 'deep dish')

import pizza as p
p.make_pizza(9, 'three cheese', 'grape fruit')
