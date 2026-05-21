class A:
    def f(self):
        print('This is f')
        return 128


a = A()
y = a.f()
print(y)

CAT = A
del A

b = CAT()
w = b.f()
print(w)

print(type(b))
