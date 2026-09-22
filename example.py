x = 1.35

from math import *

a = sin(x**(1/x))
b = cos(2 + x ** 2) + sin(2 - x**2)
c = 1 - 2 * x ** 2

y = a + b / c 
print(y)
