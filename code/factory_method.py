# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/21 23:47

from abc import ABCMeta,abstractmethod
'''
    工厂方法模式
'''

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass


class Alipay(Payment):
    def __init__(self, isHuabei = False):
        self.isHuabei = isHuabei
    def pay(self, money):
        if self.isHuabei:
            print('支付宝花呗支付了%d元' % money)
        else:
            print('支付宝支付了%d元' % money)


class Wechatpay(Payment):
    def pay(self, money):
        print('微信支付了%d元' % money)


class PaymentFactory:
    def create_payment(self,payment_method):
        if payment_method == 'Alipay':
            return Alipay()
        elif payment_method == 'Wechatpay':
            return Wechatpay()
        elif payment_method == 'Huabei':
            return Alipay(isHuabei=True)
        else:
            raise TypeError('No such payment named % s' % payment_method)


PaymentFactory().create_payment('Huabei').pay(200)