# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/24 20:19
'''
    建造者对象
'''

from abc import ABCMeta,abstractmethod


# 产品
class Player:
    def __init__(self, body=None, face=None, arm=None, leg=None):
        self.body = body
        self.face = face
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return '%s,%s,%s,%s' % (self.body,self.face,self.arm,self.leg)


# 抽象建造者
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


# 具体建造者
class GirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_body(self):
        self.player.body('苗条的身材')

    def build_face(self):
        self.player.face('漂亮的脸蛋')

    def build_arm(self):
        self.player.arm('细细的手臂')

    def build_leg(self):
        self.player.leg('大长腿')


# 具体建造者
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_body(self):
        self.player.body = '魁梧的身材'

    def build_face(self):
        self.player.face = '猴脸'

    def build_arm(self):
        self.player.arm= '肥大'

    def build_leg(self):
        self.player.leg= '粗壮'


# 指挥者
class Playerdirector():
    def builder_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_leg()
        builder.build_arm()
        return builder.player


# 客户端
builder = MonsterBuilder()
director = Playerdirector()
p = director.builder_player(builder)
print(p)