class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):  # Multiple Inheritance
    def __init__(self):
        super().__init__()  # Calls A's constructor (B's constructor is 2nd)
        # print("C")


obj = C()  # A
