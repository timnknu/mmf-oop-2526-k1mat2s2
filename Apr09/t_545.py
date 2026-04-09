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
        if isinstance(other, Vector):
            if len(self._elems) != len(other._elems):
                raise ValueError("Вектори мають різну кількість елементів")
            #assert len(self._elems) == len(other._elems)
            for i in range(len(self._elems)):
                newelems.append( self._elems[i] + other._elems[i] )
        elif isinstance(other, (float, int)):
            for i in range(len(self._elems)):
                newelems.append( self._elems[i] + other )
        else:
            raise ValueError("Невідомий тип доданка")

        r = Vector(newelems)
        return r

    def __radd__(self, other):
        #return self.__add__(other)
        return self + other

    def __mul__(self, other):
        newelems = []
        if isinstance(other, (float, int)):
            for i in range(len(self._elems)):
                newelems.append(self._elems[i] * other)
            r = Vector(newelems)
            return r
        else:
            raise ValueError("Невідомий тип співмножника")

L = [1, 2, 15]
a = Vector(L)

print(a)

print(a * 2)

