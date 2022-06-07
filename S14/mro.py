class A:

    def say_test(self):
        print("Hello from A")


class B(A):


    def say_test(self):
        print("Hello from B")


class C(B):

    def say_test(self):
        print("Hello from C")


c = C()

c.say_test()

# MRO - method resolution order

print(C.mro())