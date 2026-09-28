num = 20
mult = 1
from math import *

for n in range(1, num + 1):
    a = n ** (0.65 * n)
    b = (n-1)
    c = factorial(b)
    d = 2 * n ** 2 + c
    e = (a / d) * cos(n / pi)
    mult *= e

print(mult)