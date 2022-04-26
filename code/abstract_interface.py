# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/21 21:34

from abc import ABCMeta, abstractmethod

'''
    抽象类
'''


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self,money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print('支付宝支付了%d元' % money)


class Wechatpay(Payment):
    def pay(self, money):
        print('微信支付了%d元' % money)

p = Wechatpay()
p.pay(200)