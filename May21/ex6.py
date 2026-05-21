
def f(s, x):
    return x**2

d = {
    'pi': 3.141592,
    'square': f
}

CAT = type('MyClass', (), d)

a = CAT()

print(a.pi)
print(a.square(12))

print(type(a))