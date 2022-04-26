# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/24 23:44
'''
    组合模式
'''
from abc import ABCMeta,abstractmethod

# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点(%s, %s)' % (self.x, self.y)

    def draw(self):
        print(str(self))

# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))

# 复合组件
class Pitcture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("---- 复合图形 ----")
        for g in self.children:
            g.draw()
        print("---- 复合图形 ----")


# 客户端
Point(1,1).draw()
Line((1,2),(1,7)).draw()
Pitcture([Line((1,2),(1,7)),Point(1,1)]).draw()