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

L = [1, 2, [5, 15]]
obj = Vector(L)

print(obj)

L[-1].clear()
L.append('hello')

print(obj)
print(L)