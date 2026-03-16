# a * x**2 + b * x + c = 0
# a, b, c
# {'coef_a': ...., 'coef_b': ..., 'coef_c': ...}

def show_quadr_eq(d):
    a = d['coef_a']
    b = d['coef_b']
    c = d['coef_c']
    line_no = d['line_no']
    print('Рівняння з коефіцієнтами:', a, b, c, 'із рядка №', line_no)

def solve_quadr_eq(d):
    a = d['coef_a']
    b = d['coef_b']
    c = d['coef_c']

    if a != 0 :  # або abs(a)<1e-12
        D = b**2 - 4 * d['coef_a'] * c
        if D < 0:
            print("Розв'язків немає")
        elif D == 0: # або abs(D)<1e-12
            x0 = -b/(2*d['coef_a'])
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
        d = {'coef_a': cfs[0], 'coef_b': cfs[1], 'coef_c': cfs[2],
             'line_no': j}

        show_quadr_eq(d)
        solve_quadr_eq(d)
