# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/21 22:48

'''
    接口隔离原则:使用多个专门的接口，而不使用单一的总接口，即客户端不应该依赖那些它不需要的接口
'''
from abc import ABCMeta, abstractmethod


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print('老虎在走路...')


# 多继承
class Frag(LandAnimal,WaterAnimal):
    def walk(self):
        print('青蛙在走路...')
    def swim(self):
        print('青蛙在游泳...')


frag = Frag()
frag.swim()
frag.walk()