#Battle Handler Attempt
import random

class Monster():
    def Goblin(self, Health, Mana, Armor, Name):
        self.Health = 60
        self.Mana = 50
        self.Armor = 15
        self.Name = "Goblin"
    def Gremlin(self, Health, Mana, Armor, Name):
        self.Health = 40
        self.Mana = 120
        self.Armor = 10
        self.Name = "Gremlin"
a = random.randint(1, 50)

class MonsterPicker():
    def Picker(self, Enemy):
        self.Enemy = a
        if 26 <= a <= 50:
            d.Gremlin(9, 10, 11, 12)
            print(d.Health)
        
        if 0<= a <= 25:
            d.Goblin(9, 10, 11, 12)
            print(d.Health)



class Battle():
    def Battle1(self, Health1, MonsterName, MonsterMana, MonsterArmor):
        self.MonsterName = d.Name
        self.Health1 = d.Health
        self.MonsterMana = d.Mana
d = Monster()
f = MonsterPicker()
e = Battle()

f.Picker(a)
e.Battle1(123, 1234, 1235, 12356)
