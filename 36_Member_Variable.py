class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛 생성".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# marine_1 = Unit("마린", 40, 5)
# marine_2 = Unit("마린", 40, 5)
# tank_1 = Unit("땅크", 150, 35)

Wrath_1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(Wrath_1.name, Wrath_1.damage))

Wrath_1.clocking = True

if Wrath_1.clocking == True:
    print("클로킹")
    