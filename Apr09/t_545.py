import copy

class Vector:
    def __init__(self, elemslst):
        self._elems = copy.deepcopy(elemslst)
    def __str__(self):
        #s = ""
        # for e in self._elems:
        #     s = s + str(e) + ";"
        # s = "{" + s[:-1] + "}"
        s = '; '.join(map(str, self._elems))
        s = "(" + s + ")"
        return s
    def __add__(self, other):
        newelems = []
        if len(self._elems) != len(other._elems):
            raise ValueError("Вектори мають різну кількість елементів")
        #assert len(self._elems) == len(other._elems)
        for i in range(len(self._elems)):
            newelems.append( self._elems[i] + other._elems[i] )

        r = Vector(newelems)
        return r

L = [1, 2, 15]
a = Vector(L)

b = Vector([-8, 10, 100])

print(a)
print(b)

print(a + b)

