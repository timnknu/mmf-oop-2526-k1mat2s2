import math

x = 10
an = x
s = an
eps = 1e-5 # 10**(-5)
n = 2
while True:
    an = an * (-1) * x**2 / (2*n-2) / (2*n-1)
    s = s + an
    print(n, an, s)
    if abs(an) < eps:
        break
    n = n + 1

print(s)
print(math.sin(x))