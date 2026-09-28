num = 30
count = 0

from math import *
for n in range(1, num + 1):
    a = (pi / 2)** n 
    d = 2 * n + 1
    c = factorial(d)
    b = a / c 
    q = n * b * sin(n)
    count += q

print(q)


    

