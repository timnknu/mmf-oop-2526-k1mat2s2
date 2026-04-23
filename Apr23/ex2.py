import math

N = 1000
x = 30
an = x
s = an
for n in range(2, N+1):
    an = an * (-1) * x**2 / (2*n-2) / (2*n-1)
    s = s + an
    print(n, an, s)
print(s)
print(math.sin(x))