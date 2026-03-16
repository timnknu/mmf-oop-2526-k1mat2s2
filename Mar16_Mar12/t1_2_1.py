# a * x**2 + b * x + c = 0
# a, b, c

#def solve_quadr_eq(a, b, c):

s = '   hello world a b c 1222  \n '
print(f'strip: |{s.strip()}|')
print(f'strip: |{s.rstrip()}|')

with open('input01.txt') as f:
    for line in f:
        print(line.rstrip())