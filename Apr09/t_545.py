class Vector:
    def __init__(self, elemslst):
        self._elems = elemslst
    def __str__(self):
        #s = ""
        # for e in self._elems:
        #     s = s + str(e) + ";"
        # s = "{" + s[:-1] + "}"
        s = '; '.join(map(str, self._elems))
        s = "(" + s + ")"
        return s

L = [1, 2, 5]
obj = Vector(L)

print(obj)