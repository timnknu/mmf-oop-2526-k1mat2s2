# a * x**2 + b * x + c = 0
# a, b, c



with open('input01.txt') as f:
    for line in f:
        s = line.strip()
        if len(s) == 0:
            continue
        d = s.split()
        coefs = list(map(int, d))
        a, b, c = coefs
        print(a, b, c)