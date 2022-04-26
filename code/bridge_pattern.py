# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/24 23:17
'''
    桥模式
'''

from abc import ABCMeta,abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self):
        pass


class Rectangle(Shape):
    name = '长方形'

    def draw(self):
        # 长方形的具体逻辑 ....
        self.color.paint(self)


class Circle(Shape):
    name = '圆形'

    def draw(self):
        # 圆形的具体逻辑 ....
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print('红色的' + shape.name)


class Blue(Color):
    def paint(self, shape):
        print('蓝色的' + shape.name)


Rectangle(Red()).draw()
Circle(Blue()).draw()