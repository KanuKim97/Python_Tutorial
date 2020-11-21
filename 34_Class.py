class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛 생성".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

marine_1 = Unit("마린", 40, 5)
marine_2 = Unit("마린", 40, 5)
tank_1 = Unit("땅크", 150, 35)