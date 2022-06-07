class A:
    def __init__(self) -> None:
        print("A class")
        self.x = 10


class B: 
    def __init__(self) -> None:
        print("B class")
        self.y = 20


# problema diamatului

class A:
    def __init__(self):
        print("A.__init__")
class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()
class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()
class D(C, B):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
