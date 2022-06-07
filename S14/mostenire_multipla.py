class A:
    def __init__(self) -> None:
        print("A class")
        self.x = 10


class B: 
    def __init__(self) -> None:
        print("B class")
        self.y = 20



class C(B, A):
    pass

c = C()

print(c)