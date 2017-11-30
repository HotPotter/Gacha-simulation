import json

'''BoxSimA configuration - USER INPUT'''
a_fragments_per_slot = 1 # number of fragments in one slot
slots_num = 2 # number of slots in a box
prob_delta = 2 # Probability change after each draw
prob_delta_cap = 30 # Cap for probability change
player_num = 100 # number of players to simulate


""" INITIAL POOL - USER INPUT"""
pool_config = {"NUTCRACKER": 1,
                     "t1": 1,
                     "y1": 0,
                     "t2": 1,
                     "MISTY": 0,
                     "ODUS": 0,
                     "t3": 1,
                     "y2": 1,
                     "y3": 0,
                     "n1": 'n',
                     "n2": 'n',
                     "n3": 'n'}


"""PROBABILITY MAP"""
prob_map = {"NUTCRACKER":10,
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

f_hero= json.load(open("config/config_hero.json", 'r'))
hero_data=f_hero['heroes']
heroes = {}
for hero in hero_data:
    heroes[hero['name']] = hero['fragment']

