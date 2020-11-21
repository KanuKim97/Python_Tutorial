class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]"\
            .format(self.name, location, self.speed))


class AttackUnit(Unit):    
    def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 공격합니다. [공격력{2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

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

class BulidingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BulidingUnit("서플", 500, "7시")