# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/24 22:58
'''
    适配器模式 - 类适配器
'''

class Payment:
    def pay(self, money):
        raise NotImplementedError


class AliPay(Payment):
    def pay(self, money):
        print('支付宝支付了%d元' % money)


class WechatPay(Payment):
    def pay(self, money):
        print('微信支付了%d元' % money)


class BankPay:
    def cost(self, money):
        print('银联支付%d' % money)


class ApplePay:
    def cost(self, money):
        print('苹果支付了%d' % money)


class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(BankPay())
p.pay(200)