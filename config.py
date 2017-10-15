import json
from collections import defaultdict

'''simulation configuration - USER INPUT'''
fragments_per_box = 5
pool_name = 'remove'
num_players = 1



'''hero fragments in PickAndRemove pool - USER INPUT'''
heroes_p_remove = {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}


'''hero fragment drop probability in PickAndReturn pool - USER INPUT'''
heroes_p_return= {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}


'''Load hero configuration'''

f_hero= json.load(open("config_hero.json", 'r'))
hero_data=f_hero['heroes']
heroes = defaultdict(dict)
for hero in hero_data:
    heroes[hero['name']] = hero['fragment']







