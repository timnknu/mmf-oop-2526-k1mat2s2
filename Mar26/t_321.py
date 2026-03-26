import math


class EquationSolutions:
    def __init__(self, list_of_elements, all_real_numbers):
        if all_real_numbers:
            self._all_R = True
        else:
            self._storage = tuple(list_of_elements)
            self._all_R = False
    def show_me(self):
        print("Hi! I'm prsenting roots of the equation")
        if self._all_R:
            print('Any real number is a root!')
        else:
            if len(self._storage) == 0:
                print('There are no roots')
            else:
                print("Roots:", self._storage)
    def get_number_of_roots(self):
        if self._all_R:
            return math.inf
        else:
            return len(self._storage)


class LinearEquation:
    def __init__(self, coef_b, coef_c):
        self._b = coef_b
        self._c = coef_c
    def solve(self):
        # self.b * x + self.c == 0
        if self._b != 0:
            x = -self._c / self._b
            obj = EquationSolutions([x], all_real_numbers=False)
            return obj
        else:
            # сюди програма попадає, коли self.b == 0
            if self._c != 0:
                obj = EquationSolutions([], all_real_numbers=False)
                return obj
            else:
                obj = EquationSolutions([], all_real_numbers=True)
                return obj
#
e = LinearEquation(0, 1)
xs = e.solve()
xs.show_me()
print(xs.get_number_of_roots())