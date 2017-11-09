import json
import pool_selections as p
from pprint import pprint



'''BoxSimA configuration - USER INPUT'''
a_fragments_per_slot = 1
a_draw_logic_name = 'return'  # call hero factory, choose 'return' or 'remove*
a_pool_name = p.initial_1  # get from pool_selection
slots_num = 2 # number of slots in the box
boxes_num = 3 # number of boxes to open

# '''BoxSimB configuration - USER INPUT'''
# b_fragments_per_slot = 1
# b_draw_logic_name = 'return'  # call hero factory, choose 'return' or 'remove*
# b_pool_name = p.initial_1  # get from pool_selection

# '''BoxSimC configuration - USER INPUT'''
# c_fragments_per_slot = 1
# c_draw_logic_name = 'return'  # call hero factory, choose 'return' or 'remove*
# c_pool_name = p.initial_1  # get from pool_selection


#num_players = 1
#plot_name = 'first_hero_box' # choose between 'first_hero_box' and 'first_hero_name*









# FIXME stop condition choices here


''' fragments in PickAndRemove pool - USER INPUT'''
heroes_p_remove = {"tiffy":5, "kimmy":5, "yeti":5, "troll":5, "toffee":5, "licorice":5}


'''hero fragment drop probability in PickAndReturn pool - USER INPUT'''
heroes_p_return= {"tiffy":50, "kimmy":5, "yeti":10, "troll":10, "toffee":15}


'''Load hero configuration'''

f_hero= json.load(open("config_hero.json", 'r'))
hero_data=f_hero['heroes']
heroes = {}
for hero in hero_data:
    heroes[hero['name']] = hero['fragment']







