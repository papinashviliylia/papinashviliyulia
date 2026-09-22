from math import *
a = 0.1
b = 0.7
step = 0.05
n = int(round((b - a)/ step)) + 1
print(f"{'x':>7} | {'y':>10}")
print("-" * 20)

for i in range(n):
    x = a + i * step
    c = acos(2*x**3) / asin(x/(2*pi))
    d = 4 * abs(cos(x))/sin(2*x)
    p = c - d
    y = p ** (1/3)
    print(f"{x:7.2f} | {y:10.5f}")
