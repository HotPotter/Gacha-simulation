import config
from pprint import pprint
from collections import defaultdict , Counter, OrderedDict
'''import external files'''
import random
import plot
import pool
import inventory
import convert_csv

def has_reward(): # FIXME need to be replaced by box giving mechanism
    if random.randint(1, 1):
        return True
    else:
        return False

def simulate_open_boxes():
    result = defaultdict(list)
    num_boxes = 0
    player_inventory = inventory.Inventory()
    hero_pool = pool.PoolFactory.create_pool(config.pool_name) # modify in Config

    while True:
        num_boxes += 1
        if has_reward():
            reward = hero_pool.random_choice(pick=config.fragments_per_box)
            player_inventory.update(reward)

        update_result(result, player_inventory, num_boxes)
        #print(player_inventory.hero_and_fragments()) # print result of each box
        #print(result) # print hero formation after each box
        #print(reward) # print fragments drawn from each box

        if num_boxes > 100: # FIXME stop condition
            break

    return dict(result)

'''update inventory, create hero if possible'''
def update_result(result, inventory, num_boxes):
    for hero_name, num_fragments in inventory.hero_and_fragments():
        formed_heroes = []

        for more_heroes in result.values():
            formed_heroes += more_heroes

        if hero_name in formed_heroes:
            continue

        if num_fragments >= config.heroes[hero_name]: # calculate the formation of a hero
            result[num_boxes].append(hero_name)

def simulate(num_players):
    result = []
    for _ in range(num_players):
        one_player = simulate_open_boxes()
        result.append(one_player)
    return result

'''when do play get their first hero'''
def plot_first_hero_box(result):
    first_hero_box=[]
    for boxes in result:
        first_hero_box.append(min(boxes))
    d = OrderedDict(sorted(Counter(first_hero_box).items()))

    plot.plot_bar_dict(d)

'''who is the first hero'''  #FIXME cannot plot when getting two heroes from opening one box
def plot_first_hero_name(result):
    first_hero_name=[]
    for boxes in result:
        first_hero_name.append(*boxes[min(boxes)]) #FIXME, get value instead of key
    d = dict(Counter(first_hero_name))
    #print(d)
    plot.plot_bar_dict(d)

def do_plot(plot_name, result):
    if plot_name == 'first_hero_box':
        plot_first_hero_box(result)
    if plot_name == 'first_hero_name':
        plot_first_hero_name(result)


def main():
    result = simulate(config.num_players)
    #do_plot(config.plot_name, result)
    convert_csv.output_csv(result) # write result to csv file

if __name__ == '__main__':
    main()

