'''place holder
game_round_per_day = 10
pass_rate = 0.70
'''

reward_per_x_box = 5
reward_drop_rate = 0.5
fragments_per_box = 5

heroes = {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}

'''try JSON'''
heroes_json = '''{"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}'''

import json

json.loads(heroes_json)

json.dumps(heroes)

pool_name = 'return'