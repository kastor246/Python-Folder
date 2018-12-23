#Enemy Picker

import random

a = random.randint(1,60)
class MonsterPicker():
    a = random.randint(1,60)
    def Picker(self, Enemy):
        self.Enemy = a
        if 26 <= a <= 50:
            d.Gremlin(9, 10, 11, 12)
            print(d.Health)
        
        if 0<= a <= 25:
            d.Goblin(9, 10, 11, 12)
            print(d.Health)
        

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

d = Monster()
d.Gremlin(5, 6, 7, 8)
d.Goblin(1, 2, 3, 4)
