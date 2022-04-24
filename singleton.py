# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/24 21:18

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


A = MyClass(10)
B = MyClass(20)
print(A.a, B.a)
print(id(A),id(B))