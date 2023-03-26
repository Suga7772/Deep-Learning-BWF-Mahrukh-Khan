import timeit
import random


# https://note.nkmk.me/en/python-timeit-measure/#:~:text=source%3A%20timeit_module.py-,%25%25timeit,the%20time%20to%20import%20NumPy.
# creating a function
# calculates the sum of n consecutive numbers as an example, and measure its execution time.
def test(n):
    return sum(range(n))


def testes():
    return random.randint(10, 50)


starting_time = timeit.default_timer()

print("Start time :", starting_time)
testes()
print("Time difference :", timeit.default_timer() - starting_time)

n = 5000
loop = 500

result = timeit.timeit('test(n)', globals=globals(), number=69)
print(result / loop)
