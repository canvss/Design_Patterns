# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/21 22:36
'''
    里氏替换原则：子类和父类相同的方法内部实现和逻辑可能不同，但是参数和返回值是相同类型的
'''


class User:
    def show_name(self,name):
        print(name)


class VIPUser(User):
    def show_name(self,name):
        print(name)


VIPUser().show_name('Jack')