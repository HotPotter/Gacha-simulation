"""define pool logic"""
import pool_selections as p
import random
import config

class PickAndReturn():
    def __init__(self, pool_name):
        self.item_name = [] #item name
        self.ps = [] #drop probability
        for i, p in pool_name:
            self.item_name.append(i)
            self.ps.append(p)

        #self.update_pool(inventory)

    # def update_pool(self, inventory):
    #     self.initial_pool = p.initial_1
    #     if item in inventory.items():
    #         pool_name.pop('item',none)
    #         pool_name.update(p.extension_1[self.switch_count])
    #         self.switch_count +=1
    #     return pool_name

    def random_choice(self, pick): #FIXME, need to update pool (not used in simulation yet)
        return random.choices(self.item_name, self.ps, k=pick)




class PickAndRemove():  # FIXME need to update pool
    def __init__(self, pool_name):
        pool = []
        for item_name, num in pool_name:
            pool += [item_name] * num
        random.shuffle(pool)
        self.pool = pool

    def random_choice(self, pick): #FIXME, pick needs to read from config
        reward = self.pool[0:pick]
        self.pool = self.pool[pick:]
        return reward


"""define pool factory

class LogicFactory():
    @classmethod
    def create_pool(cls, pool_name, draw_logic_name):
        list_p_remove = [i for i in config.heroes_p_remove.items()]  # get data from config
        hero_config_list_p_return = [i for i in config.heroes_p_return.items()]  # get data from config
        if draw_logic_name == 'remove':
            pool = PickAndRemove(pool_name)
        elif pool_name == 'return':
            pool = PickAndReturnHeroPool(hero_config_list_p_return)
        else:
            raise ValueError('invalid pool name')
        return pool
"""



def logic_factory(draw_logic_name, pool_name):

    pool_content= [i for i in pool_name.items()]
    if draw_logic_name == 'remove':
        pool = PickAndRemove(pool_content)


    elif draw_logic_name == 'return':
        pool = PickAndReturn(pool_content)

    return pool





