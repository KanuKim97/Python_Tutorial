from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다".format(name))
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]"\
            .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):    
    def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 공격합니다. [공격력{2}]".format(self.name, location, self.damage))


class marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다 현재 Hp : {1}".format(self.name, self.hp))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))


class Tank(AttackUnit):
    seige_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "땅크", 150, 1, 35)
        self.Seige_mode = False

    def Set_Seige_mode(self):
        if Tank.seige_developed == False:
            return

        if self.Seige_mode == False:
            print("시즈모드 전환")
            self.damage *= 2
            self.Seige_mode = True
        else:
            print("시즈모드 해제")
            self.damage /= 2
            self.Seige_mode = False


class Flyable:
    def __init__(self, Speed):
        self.Speed = Speed

    def fly(self, name, location):
         print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
             .format(name, location, self.Speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, Speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, Speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = True


def Game_Start():
    print("[Alret] 새로운 게임을 시작합니다.")


def Game_Over():
    print("Player:GG")
    print("[Alret] Player가 게임에서 퇴장하였습니다")


Game_Start()

m1 = marine()
m2 = marine()
m3 = marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

Attack_Units = []
Attack_Units.append(m1)
Attack_Units.append(m2)
Attack_Units.append(m3)

Attack_Units.append(t1)
Attack_Units.append(t2)

Attack_Units.append(w1)

for unit in Attack_Units:
    unit.move("1시")

Tank.seige_developed = True
print("시즈모드 개발 완료")

for unit in Attack_Units:
    if isinstance(unit, marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.Set_Seige_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in Attack_Units:
    unit.attack("1시")

for unit in Attack_Units:
    unit.damaged(randint(5, 20))

Game_Over()