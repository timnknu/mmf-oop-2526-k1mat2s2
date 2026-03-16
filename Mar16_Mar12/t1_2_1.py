# a * x**2 + b * x + c = 0
# a, b, c

def show_quadr_eq(a, b, c):
    print('Рівняння з коефіцієнтами:', a, b, c)

def solve_quadr_eq(a, b, c):
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
    for line in f:
        s = line.strip()
        if len(s) == 0:
            continue
        d = s.split()
        coefs = list(map(int, d))
        a, b, c = coefs
        show_quadr_eq(a, b, c)
        solve_quadr_eq(a, b, c)
