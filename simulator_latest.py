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
        if pool_name == 'remove':
            pool = PickAndRemoveHeroPool(hero_config_list)
        elif pool_name == 'return':
            pool = PickAndReturnHeroPool(hero_config_list)
        else:
            raise ValueError('invalid pool name')
        return pool


'''WIP WIP WIP'''



def has_reward(): #FIXME, need to be related to reward giving mechanism
    if random.randint(0,1):
        return True
    else:
        return False

