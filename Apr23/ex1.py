import math

N = 100
x = 40.0
s = 0
for n in range(1, N+1):
    an = (-1)**(n+1) * x**(2*n-1) / math.factorial(2*n-1)
    s = s + an
    print(n, an, s, float(math.factorial(2*n-1)))
print(s)
print(math.sin(x))