import copy

class Vector:
    def __init__(self, elemslst):
        self._elems = copy.deepcopy(elemslst)
    def __str__(self):
        # s = ""
        # for e in self._elems:
        #     s = s + str(e) + ";"
        # s = "{" + s[:-1] + "}"
        s = '; '.join(map(str, self._elems))
        s = "(" + s + ")"
        return s
    def __add__(self, other):
        newelems = []
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Вектори мають різну кількість елементів")
            #assert len(self._elems) == len(other._elems)
            for i in range(len(self)):
                newelems.append( self[i] + other[i] )
        elif isinstance(other, (float, int)):
            for i in range(len(self)):
                newelems.append( self[i] + other )
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
            for i in range(len(self)):
                newelems.append(self[i] * other)
            r = Vector(newelems)
            return r
        else:
            raise ValueError("Невідомий тип співмножника")
    def __getitem__(self, item):
        return self._elems[item]
    def __setitem__(self, key, value):
        self._elems[key] = value

    def __len__(self):
        return len(self._elems)

row1 = Vector([1, 2, 15])
row2 = Vector([100, 150, 1500])

M = Vector([row1, row2])

print(M)

row3 = Vector([-15, -42, -5])
row4 = Vector([-21, -14, -35])
N = Vector([row3, row4])

print(M + N)