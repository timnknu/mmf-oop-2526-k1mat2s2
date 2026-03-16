# a * x**2 + b * x + c = 0
# a, b, c
# {'coef_a': ...., 'coef_b': ..., 'coef_c': ...}

class QuadraticEquation:
    def __init__(self, a, b, c, line_no):
        self.coef_a = a
        self.coef_b = b
        self.coef_c = c
        self.line_no = line_no

    def show_quadr_eq(self):
        a = self.coef_a
        b = self.coef_b
        c = self.coef_c
        line_no = self.line_no
        print('Рівняння з коефіцієнтами:', a, b, c, 'із рядка №', line_no)

    def solve_quadr_eq(self):
        a = self.coef_a
        b = self.coef_b
        c = self.coef_c

        if a != 0 :  # або abs(a)<1e-12
            D = b**2 - 4 * a * c
            if D < 0:
                print("Розв'язків немає")
            elif D == 0: # або abs(D)<1e-12
                x0 = -b/(2*a)
                print("Розв'язок:", x0)
            else:
                x1 = (-b - D**0.5)/(2*a)
                x2 = (-b + D**0.5)/(2*a)
                print("Розв'язки:", x1, x2)
            #
        else:
            print('Це не квадратне рівняння')



with open('input01.txt') as f:
    j = 0
    for line in f:
        s = line.strip()
        j += 1
        if len(s) == 0:
            continue
        d = s.split()
        cfs = list(map(int, d))
        e = QuadraticEquation(cfs[0], cfs[1], cfs[2], j)
        e.show_quadr_eq()
        e.solve_quadr_eq()
