# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/25 22:33
'''
    责任链模式
'''
from abc import ABCMeta,abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print('总经理准假%d天' % day)
        else:
            print('你还是辞职吧！')


class DepartmentManager(Handler):
    def __init__(self):
        self.__next = GeneralManager()

    def handle_leave(self, day):
        if day <= 7:
            print('部门经理准假%d天' % day)
        else:
            self.__next.handle_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.__next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print('项目主管准假%d天' % day)
        else:
            self.__next.handle_leave(day)


handler = ProjectDirector()
handler.handle_leave(11)