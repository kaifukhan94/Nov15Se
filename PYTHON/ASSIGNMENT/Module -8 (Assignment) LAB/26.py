# 26) Write a Python program to show hybrid inheritance. 


class A:
    def a(self):
        print("Class A")

class B(A):
    def b(self):
        print("Class B")

class C(A):
    def c(self):
        print("Class C")

class D(B, C):
    def d(self):
        print("Class D")

obj = D()
obj.a()
obj.b()
obj.c()
obj.d()