#Main Game

import os
import time
import sys
import random


Clear = lambda: os.system('cls') #Clears console of text

class Player():
    Name = ()
    def Orc(self, Health, Armor, Magic):
        self.Health = 100
        self.Armor = 30
        self.Magic = 25
    def Human(self, Health, Armor, Magic):
        self.Health = 65
        self.Armor = 18
        self. Magic = 35
    def Elf(self, Health, Armor, Magic):
        self.Health = 55
        self.Armor = 15
        self.Magic = 45



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

class Inventory1:
    def __init__(self, Items):
        self.Items = []

    def Acquired(self, add):
        self.add = Inventory.Items.append(add)

    def reit(self, delete):
        self.delete = Inventory.Items.pop(delete)

Inventory = Inventory1("Items")

User = Player()
Fight = Monster()
Fight.Goblin(3, 4, 5, 6)

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


class Attacks():
    def Attack1(self, Attack4):
        self.Attack4 = 20
    def Attack2(self,Attack3):
        self.Attack3 = "30"

class Battle():
    def Battle1(self, Health1, MonsterName, MonsterMana, MonsterArmor):
        self.MonsterName = d.Name
        self.Health1 = d.Health
        self.MonsterMana = d.Mana
    def Battle2(self, Health2, PlayerName, PlayerMana, PlayerArmor):
        self.Health2 = User.Health
        self.PlayerName = User.Name
        self.PlayerMana = User.Magic
        self.PlayerArmor = User.Armor
    def EnenemyAttack(self, HealthResult, ManaResult, ArmorResult):
        self.HealthResult = Health2 - b.Attack1
d = Monster()
f = MonsterPicker()
e = Battle()
b = Attacks()

f.Picker(a)
e.Battle1(123, 1234, 1235, 12356)

print("Welcome!")
print("V. 0.1")

Clear()

print("1. Play")
print("2. Quit")
a = input("Select one: ")

if a == "1":
    print("Let's begin")
    time.sleep(2)
    User.Name = input("What is your name? ")
    GameState = True
    a = input("What class are you? 1. Human, 2. Orc, 3. Elf ")
    if a == "1":
        User = User.Human(1, 2, 3)
    elif a == "2":
        User = User.Orc(1, 2, 3)
    elif a == "3":
        User = User.Elf(1,2,3)
        

    
elif a == "2":
    print("Sorry to see you go.")
    time.sleep(2)
    print("Farewell~")
    time.sleep(2)
    Clear()
    time.sleep(3)
    sys.exit2
    
while GameState == True:
    print("You awaken, laying atop your bed..")
    print("The sun is shining gleefully inside your cabin..")
    a = input("Do you, 1. Head outside, or 2. Look inside your dresser? ")
    if a == "1":
        print("You walk outside, and see a Gremlin! It's terrorizing the "
              "local cattle!")
    elif a == "2":
        print("You find: Short Sword")
        b = input("Do you take it? ")
        if b == "Y":
            Inventory.Aqcuired("Short Sword")
    
            
    
    
