#coding: utf-8
# import os

# os.system("pyinstaller -i=Naruto.ico -F clear.py")
# os.system("pyinstaller -F clear.py")

class A(object):
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        super().m()

class C(A):
    def m(self):
        print("m of C called")
        super().m()

class D(B,C):
    def m(self):
        print("m of D called")
        super().m()

print(D.__mro__)