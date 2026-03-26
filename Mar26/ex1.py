class A:
    def __init__(self):
        self.x = 12
    def show(self):
        print("I am class A, my x is ", self.x)


class B(A):
    def __init__(self):
        self.x = 35

obj = B()

obj.show()

