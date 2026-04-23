import math

def sg(x, eps = 1e-5):
    an = x
    yield an
    n = 2
    while True:
        an = an * (-1) * x**2 / (2*n-2) / (2*n-1)
        if abs(an) < eps:
            break
        #
        yield an
        n = n + 1


###########

x = 5.0
s = 0
#for an in sg(x, eps=1e-7):
for an in sg(x):
    #print(an)
    s = s + an
print(s)
print(math.sin(x))
