# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/25 23:31

'''
    策略模式
'''

from abc import ABCMeta,abstractmethod

# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass

# 具体策略
class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)

# 上下文
class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


# Client
data = '[...]'
s1 = FastStrategy()
s2= SlowStrategy()

context = Context(s1,data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()