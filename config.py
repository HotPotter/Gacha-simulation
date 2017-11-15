import json

'''BoxSimA configuration - USER INPUT'''
a_fragments_per_slot = 1 # number of fragments in one slot
slots_num = 2 # number of slots in a box
prob_delta = 1 # Probability change after each draw
prob_delta_cap = 10 # Cap for probability change
player_num = 1 # number of players to simulate



""" INITIAL POOL - USER INPUT"""
resource_initial = ['NUTCRACKER', 't1', 'y1', 't2','y3','t3']

"""EXTENSION POOL - USER INPUT"""
resource_expansion = ['ODUS', 'y2','MISTY']

"""EXTENSION COSTUME POOL"""
resource_costume_nc = ['n1', 'n2', 'n3']



"""PROBABILITY MAP"""
resource_all = {"NUTCRACKER":10,
                "t1":10,
                "y1":10,
                "t2":10,
                "MISTY":10,
                "ODUS":10,
                "t3":10,
                "y2":10,
                "y3":10,
                "n1":10,
                "n2":10,
                "n3":10}


"""Load hero configuration"""

f_hero= json.load(open("config_hero.json", 'r'))
hero_data=f_hero['heroes']
heroes = {}
for hero in hero_data:
    heroes[hero['name']] = hero['fragment']

"""COMPLETION MAP"""
item_map = {}
for i in resource_all:
    item_map[i]= 0


"""INVENTORY MAP"""
inventory_map = {}
for i in resource_all:
    inventory_map[i] = 0
