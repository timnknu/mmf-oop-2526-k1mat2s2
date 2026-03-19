# a * x**2 + b * x + c = 0
# a, b, c

class QuadraticEquation:
    def __init__(self, data, line_no):
        if isinstance(data, str): # чи містить змінна data щось, що ми звикли називати "текстовий рядок" ?
            #print('нам передали в змінній data текстовий рядок')
            d = data.split()
            cfs = list(map(int, d))
            self.coef_a = cfs[0]
            self.coef_b = cfs[1]
            self.coef_c = cfs[2]
            self.line_no = line_no
        elif isinstance(data, list): # чи містить змінна data щось, що ми звикли називати "список" ?
            #print('нам передали в змінній data текстовий список')
            self.coef_a = data[0]
            self.coef_b = data[1]
            self.coef_c = data[2]
            self.line_no = line_no
        elif isinstance(data, QuadraticEquation): # чи містить змінна data щось, що є вже кимось раніше створеним квадратним рівнянням?
            self.coef_a = data.coef_a
            self.coef_b = data.coef_b
            self.coef_c = data.coef_c
            self.line_no = data.line_no
        else:
            print('нам передали в змінній data щось, з чим ми не вміємо працювати!')
            raise ValueError


    def show_quadr_eq(self):
        print('Рівняння з коефіцієнтами:', self.coef_a, self.coef_b, self.coef_c,
              'із рядка №', self.line_no)

    def solve_quadr_eq(self):
        if self.coef_a != 0 :  # або abs(a)<1e-12
            D = self.coef_b**2 - 4 * self.coef_a * self.coef_c
            if D < 0:
                print("Розв'язків немає")
                return []
            elif D == 0: # або abs(D)<1e-12
                x0 = -self.coef_b/(2*self.coef_a)
                print("Розв'язок:", x0)
                return [x0]
            else:
                x1 = (-self.coef_b - D**0.5)/(2*self.coef_a)
                x2 = (-self.coef_b + D**0.5)/(2*self.coef_a)
                print("Розв'язки:", x1, x2)
                return [x1, x2]
            #
        else:
            print('Це не квадратне рівняння')
            return None

##


equations_lst = []

# зчитування рівнянь із файла
with open('input01.txt') as f:
    j = 0
    for line in f:
        s = line.strip()
        if len(s) == 0:
            continue
        j += 1

        e = QuadraticEquation(line, j)
        equations_lst.append(e)

# аналізу зчитаних рівнянь -- друкуватимемо лише ті, які мають 1 розв'язок
equations_with_one_root = []
for eq in equations_lst:
    roots = eq.solve_quadr_eq()
    if isinstance(roots, list):
        if len(roots)==1:
            equations_with_one_root.append(eq)
print(f'Загалом було {len(equations_with_one_root)} рівнянь з одним розв"язком')