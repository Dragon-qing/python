class A(object):
    def __init__(self):
        self.num = 1

    def print_info(self):
        print(self.num)


class C(object):
    def __init__(self):
        self.num = 2

    def print_info(self):
        print(self.num)


class B(A, C):

    pass


result = B()
result.print_info()
print(B.__mro__)