# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/22 0:03

'''
    抽象工厂模式
'''

from abc import ABCMeta, abstractmethod


# ----抽象产品----
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class PhoneCPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class PhoneOS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# ----具体的产品----
class SmallShell(PhoneShell):
    def show_shell(self):
        print('普通小手机壳')


class BigShell(PhoneShell):
    def show_shell(self):
        print('普通大手机壳')


class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果手机壳')


class SnapDragonCPU(PhoneCPU):
    def show_cpu(self):
        print('骁龙CPU')


class HuaweiCPU(PhoneCPU):
    def show_cpu(self):
        print('华为CPU')


class AppleCPU(PhoneCPU):
    def show_cpu(self):
        print('苹果CPU')


class AndroidOS(PhoneOS):
    def show_os(self):
        print('安卓系统')

class AppleOS(PhoneOS):
    def show_os(self):
        print('ios系统')


# ---- 抽象工厂----
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass
    @abstractmethod
    def make_cpu(self):
        pass
    @abstractmethod
    def make_os(self):
        pass


# ----具体工厂----
class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return AppleOS()


class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_cpu(self):
        return HuaweiCPU()

    def make_os(self):
        return AndroidOS()


class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_phone_info(self):
        print('Phone INFO：')
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()


def make_phone(factory):
    shell = factory.make_shell()
    cpu = factory.make_cpu()
    os = factory.make_os()
    return Phone(shell, cpu, os)


apple = make_phone(AppleFactory())
apple.show_phone_info()