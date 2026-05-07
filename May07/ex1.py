def g():
    print('g starts')
    a = 1 / 0
    print('g ready')

def f():
    pass
    print('f starts')
    g()
    print('f ready')

def main():
    pass
    print('main starts')
    try:
        f()
    except:
        print('error')
    print('main ready')

print('main program begins')
#try:
main()
# except:
#     print('error')
print('main program ends')