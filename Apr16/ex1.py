L = [1,2,3]
d = {'hello': 'cat', 'pi': 3.14}
t = (1, 10, 500)
s = 'hello world'
c = set([1, 1, 1, 50]) # буде {1, 50}

for e in L:
    print(e)

for e in d:
    print(e)

for e in t:
    print(e)

for e in s:
    print(e)

for e in c:
    print(e)

for e in range(1, 5):
    print(e)

A = set(dir(L))
A = A.intersection(set(dir(d)))
A = A.intersection(set(dir(t)))
A = A.intersection(set(dir(s)))
A = A.intersection(set(dir(range(1, 5))))
print(A)