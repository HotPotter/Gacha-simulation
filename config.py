import json

reward_per_x_box = 5
reward_drop_rate = 0.5
fragments_per_box = 5

heroes = {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}

'''try JSON'''
heroes_json = '''{"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}'''

f_hero= json.load(open("config_hero.json", 'r'))

h=json.dumps(f_hero)

print(f_hero['heroes'])



pool_name = 'return'