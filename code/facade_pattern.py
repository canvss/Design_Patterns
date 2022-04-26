# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/25 21:46
'''
    外观模式
'''

# 子类系统
class Cpu:
    def run(self):
        print('CPU开始运行')

    def stop(self):
        print('CPU停止运行')


class Disk:
    def run(self):
        print('硬盘开始运行')

    def stop(self):
        print('硬盘停止运行')


class Memory:
    def run(self):
        print('内存开始工作')

    def stop(self):
        print('内存停止工作')

# 外观
class Computer:
    def __init__(self):
        self.cpu = Cpu()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# Client
computer = Computer()
computer.run()
computer.stop()
