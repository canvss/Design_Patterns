# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/21 23:23
'''
    简单工厂模式
'''
from abc import ABCMeta,abstractmethod


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


class Bankpay(Payment):
    def pay(self,money):
        print('银行卡支付了%d元' % money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatpayFactory(PaymentFactory):
    def create_payment(self):
        return Wechatpay()


class HuabeipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(isHuabei=True)


class BankpayFactory(PaymentFactory):
    def create_payment(self):
        return Bankpay()


pay = WechatpayFactory().create_payment()
pay.pay(500)