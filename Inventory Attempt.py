#First Attempt at creating an Inventory System

class Inventory:
    def __init__(self, Items):
        self.Items = []

    def Acquired(self, add):
        self.add = Inventory.Items.append(add)

    def reit(self, delete):
        self.delete = Inventory.Items.pop(delete)

Inventory = Inventory("Items")
        



