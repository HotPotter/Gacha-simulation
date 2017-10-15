'''define pool logic'''
import config
import random

class PickAndReturnHeroPool():
    def __init__(self, hero_config_p):
        self.heroes = [] #hero name
        self.ps = [] #drop probability
        for hero, p in hero_config_p:
            self.heroes.append(hero)
            self.ps.append(p)

    def random_choice(self, pick): #FIXME, pick needs to read from config
        return random.choices(self.heroes, self.ps, k=pick)

class PickAndRemoveHeroPool():
    def __init__(self, hero_config_p):
        pool = []
        for hero_name, num in hero_config_p:
            pool += [hero_name] * num
        random.shuffle(pool)
        self.pool = pool

    def random_choice(self, pick): #FIXME, pick needs to read from config
        reward = self.pool[0:pick]
        self.pool = self.pool[pick:]
        return reward



'''define pool factory'''

class PoolFactory():
    @classmethod
    def create_pool(cls, pool_name):
        hero_config_list_p_remove = [i for i in config.heroes_p_remove.items()]  # get data from config
        hero_config_list_p_return = [i for i in config.heroes_p_return.items()]  # get data from config
        if pool_name == 'remove':
            pool = PickAndRemoveHeroPool(hero_config_list_p_remove)
        elif pool_name == 'return':
            pool = PickAndReturnHeroPool(hero_config_list_p_return)
        else:
            raise ValueError('invalid pool name')
        return pool