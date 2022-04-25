# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/25 22:00
from abc import ABCMeta,abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print('初始化RealSubject class.')
        f = open(filename, 'r', encoding='utf-8')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):
    def __init__(self, filename):
        self.subj = None
        self.filename = filename

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限')


virtual = VirtualProxy('test.txt')
content = virtual.get_content()
print(content)
virtual.set_content('你好世界！')

protected = ProtectedProxy('test.txt')
content = protected.get_content()
print(content)
protected.set_content('hello world!')