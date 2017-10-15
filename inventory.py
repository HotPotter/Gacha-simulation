'''define player inventory - hero possession'''
from collections import defaultdict

class Inventory():
    def __init__(self):
        self.inventory = defaultdict(int)
        self.coins = 1000

    def update(self, reward):
        for hero_name in reward:
            self.inventory[hero_name] += 1

    def hero_and_fragments(self):
        return self.inventory.items()


