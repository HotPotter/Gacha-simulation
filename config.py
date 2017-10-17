import json
from collections import defaultdict

'''simulation configuration - USER INPUT'''
fragments_per_box = 2
pool_name = 'remove'  # call hero factory, choose 'return' or 'remove*
num_players = 1000
plot_name = 'first_hero_box' # choose between 'first_hero_box' and 'first_hero_name*



'''hero fragments in PickAndRemove pool - USER INPUT'''
heroes_p_remove = {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}


'''hero fragment drop probability in PickAndReturn pool - USER INPUT'''
heroes_p_return= {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}


'''Load hero configuration'''

f_hero= json.load(open("config_hero.json", 'r'))
hero_data=f_hero['heroes']
heroes = {}
for hero in hero_data:
    heroes[hero['name']] = hero['fragment']







