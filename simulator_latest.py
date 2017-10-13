import config
from pprint import pprint
from collections import defaultdict
import random


'''define pool logic'''

#FIXME, need to separate drop rate from hero composition number, read drop rate from config
class PickAndReturnHeroPool():
    def __init__(self, hero_config):
        self.heroes = [] #hero name
        self.ps = [] #drop probability
        for hero, p in hero_config:
            self.heroes.append(hero)
            self.ps.append(p)

    def random_choice(self, pick=1): #FIXME, pick needs to read from config
        return random.choices(self.heroes, self.ps, k=pick)

class PickAndRemoveHeroPool():
    def __init__(self, hero_config):
        pool = []
        for hero_name, num in hero_config:
            pool += [hero_name] * num
        random.shuffle(pool)
        self.pool = pool

    def random_choice(self, pick=1): #FIXME, pick needs to read from config
        reward = self.pool[0:pick]
        self.pool = self.pool[pick:]
        return reward



'''define pool factory'''

class PoolFactory():
    @classmethod
    def create_pool(cls, pool_name):
        hero_config_list = [i for i in config.heroes.items()]  # get data from config
        if pool_name == 'remove':
            pool = PickAndRemoveHeroPool(hero_config_list)
        elif pool_name == 'return':
            pool = PickAndReturnHeroPool(hero_config_list)
        else:
            raise ValueError('invalid pool name')
        return pool


'''define player inventory - hero possession'''


class Inventory():  # need to add
    def __init__(self):
        self.inventory_hero = defaultdict(int)  # starts as empty
        self.inventory_coin = 0  # soft currency

    def update(self,reward):
        for hero_name in reward:
            self.inventory_hero[hero_name] += 1

    def hero_and_fragment(self):
        return self.inventory_hero.items()



def has_reward(): #FIXME, need to be related to reward giving mechanism
    if random.randint(0,1):
        return True
    else:
        return False


def simulate_open_box():
    result = defaultdict(list)
    num_boxes = 0
    player_inventory = Inventory()
    hero_pool= PoolFactory.create_pool('remove') #FIXME, need to pick from config

    while True: # Pick logic
        num_boxes += 1
        if has_reward():
            reward = hero_pool.random_choice(pick=config.fragments_per_box) # Choose how many pieces in a box
            player_inventory.update(reward)

        update_result(result, player_inventory, num_boxes)

        if num_boxes > 5000: #FIXME, stop condition, need to read from config
            break

    return dict(result)


def update_result(result,inventory,num_boxes): #Create a hero where there are enough fragments
    for hero_name, num_fragments in inventory.hero_and_fragment():
        formed_heroes = []

        for more_heroes in result.values():
            formed_heroes += more_heroes

        if hero_name in formed_heroes:
            continue

        if num_fragments >= config.heroes[hero_name]:
            result[num_boxes].append(hero_name)

'''define how many times to run the simulation'''
def simulate(num_players):
    result = []
    for _ in range(num_players):
        days = simulate_open_box()
        result.append(days)
    return result


def plot(result):
    print('Here is the result:')
    pprint(result)

def main():
    result = simulate(1)
    plot(result)

if __name__ == '__main__':
    main()