# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/24 22:52
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


class NewBankPay(Payment,BankPay):
    def pay(self, money):
        self.cost(money)

    def cost(self, money):
        print('银联支付%d' % money)

p = NewBankPay()
p.pay(200)