# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/25 23:00
'''
    观察者模式
'''
from abc import ABCMeta, abstractmethod

# 抽象订阅者
class Observer(metaclass=ABCMeta):
    # notice是一个Notice类的对象
    def update(self, notice):
        pass

# 抽象发布者
class Notice:
    def __init__(self):
        self.observer = []

    def attach(self, obs):
        self.observer.append(obs)

    def detach(self, obs):
        self.observer.remove(obs)
    # 推送
    def notify(self):
        for obs in self.observer:
            obs.update(self)

# 具体发布者
class StaffNotice(Notice):
    def __init__(self, company_info = None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        # 推送
        self.notify()

# 具体订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# Client
notice = StaffNotice("初始化公司")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = '明天公司放假！！！'
print(s1.company_info)
print(s2.company_info)