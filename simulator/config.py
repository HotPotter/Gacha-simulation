import json

pool_config_json = json.load(open('config/pool_config.json', 'r'))

'''BoxSimA configuration - USER INPUT'''
a_fragments_per_slot = pool_config_json['a_fragments_per_slot']# number of fragments in one slot
slots_num = pool_config_json['slots_num'] # number of slots in a box
prob_delta = pool_config_json['prob_delta'] # Probability change after each draw
prob_delta_cap = pool_config_json['prob_delta_cap'] # Cap for probability change
player_num = pool_config_json['player_num'] # number of players to simulate


pool_config = pool_config_json['pool_config']

prob_map = pool_config_json['prob_map']


"""Load hero configuration"""

f_hero= json.load(open("config/hero_config.json", 'r'))
hero_data=f_hero['heroes']
heroes = {}
for hero in hero_data:
    heroes[hero['name']] = hero['fragment']

