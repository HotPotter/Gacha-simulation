import random
from simulator import config
from pprint import pprint
import pandas as pd


class Inventory():
    def __init__(self,
                 heroes_cfg):
        self.id = id
        self.heroes_cfg = heroes_cfg
        self.inventory = {k:0 for k,v in heroes_cfg.items()}
        self.completion = list()
        self.completion_matrix = {k:0 for k,v in heroes_cfg.items()}

    def get_inventory(self):
        return self.inventory

    def _update_completion(self):
        for item, val in self.inventory.items():
            if item not in self.completion:
                if val >= self.heroes_cfg[item]: # >= to add to completion when overdrawn
                    self.completion.append(item)
                    self.completion_matrix[item] = 1

    def update(self, reward):
        #TODO consider case of overdraw
        for item in reward:
            self.inventory[item] += 1
            self._update_completion()


class Pool():
    def __init__(self,
                 pool_config,
                 prob_map,
                 prob_delta,
                 prob_deltacap,
                 inventory
                 ):
        self.pool_config = pool_config  # a dict
        self.prob_map = prob_map
        self.inventory = inventory  # this is a dict
        self.prob_delta = prob_delta
        self.prob_deltacap = prob_deltacap
        self._create_pool_list()
        self.pool_add_list = [i for i, v in self.pool_config.items() if v == 0]

    def _create_pool_list(self):
        self.pool_list = list()
        for item, val in self.pool_config.items():
            if val == 1:
                self.pool_list.append(item)

    def _update_prob(self):
        for item, val in self.inventory.inventory.items():
            if self.inventory.inventory[item] < self.prob_deltacap:
                self.prob_map[item] += self.prob_delta

    def _update_pool_list(self):
        for item in self.inventory.completion:  # inventory.completion is a list
            if item in self.pool_list:
                self.pool_list.remove(item)  # remove completed item from pool list
                if item == 'NUTCRACKER' and self.pool_config['NUTCRACKER'] != 'done' :
                    self.pool_add_list += [i for i, v in self.pool_config.items() if v == 'n']
                random.shuffle(self.pool_add_list)  # shuffle items, prepare to get a new item
                self.pool_config[item] = 'done'  # set pool config
                if len(self.pool_add_list) > 0:
                    self.pool_list.append(self.pool_add_list.pop(0))

    def update_pool(self):
        self._update_prob()
        self._update_pool_list()

    def is_empty(self):
        return len(self.pool_list) == 0


class DrawFromBox():
    def __init__(self,
                 fragments_num,
                 slots_num,
                 pool_list,
                 prob_map# dict, value is probability
                 ):
        assert type(slots_num) == int
        assert type(fragments_num) == int
        assert type(pool_list) == list
        self.slots_num = slots_num
        self.fragment_num = fragments_num
        self.pool_list = pool_list
        self.prob_map = prob_map
        self.reward = list()

    def get_reward(self):
        item_name = self.pool_list
        item_prob = []
        for i in self.pool_list:
            item_prob.append(self.prob_map[i])
        self.reward = random.choices(item_name, item_prob, k=self.fragment_num)
        # except Exception as e:
        #     print(e)
        return self.reward


class PlayerProfile():
    def __init__(self,
                 skill_rating,  # multiplier to passrate
                 progression,
                 inventory,
                 pool
                 ):
        self.id = 0
        self.skill_rating = skill_rating
        self.progression = progression
        self.inventory = inventory  # an instance of class Inventory
        self.pool = pool  # an instance of class Pool

    def update_id(self):
        pass


class BoxGet():  # determine if a box is given on an attempt
    def __init__(self,
                 drop_rate
                 ):
        self.drop_rate = drop_rate

    def drop_box(self):
        if random.random() < self.drop_rate:
            return True
        else:
            return False


class Simulation():
    def __init__(self,
                 fragments_num,
                 slots_num,
                 pool_config,
                 prob_map,
                 prob_delta,
                 prob_deltacap,
                 heroes_cfg
                 ):
        self.fragments_num = fragments_num
        self.slots_num = slots_num
        self.heroes_cfg = heroes_cfg
        self.inventory = Inventory(self.heroes_cfg)

        self.pool = Pool(pool_config,
                         prob_map,
                         prob_delta,
                         prob_deltacap,
                         self.inventory)

        self.draw_from_box = DrawFromBox(self.fragments_num,
                                         self.slots_num,
                                         self.pool.pool_list,
                                         self.pool.prob_map)
        self.box_id = 1


    def update_box_id(self):
        self.box_id += 1

    def run(self):
        result_matrix = []
        while self.pool.is_empty() is not True:
            for n in range(0,self.slots_num): # one box
                draw = self.draw_from_box.get_reward()
                self.inventory.update(draw)
                self.pool.update_pool()
            inventory_matrix = [v for i,v in self.inventory.inventory.items()]
            completion_matrix = [v for i,v in self.inventory.completion_matrix.items()]
            result_matrix_box = inventory_matrix + completion_matrix
            result_matrix_box.insert(0,self.box_id)
            result_matrix.append(result_matrix_box)
            self.update_box_id()
        return (result_matrix)


class OutputFormat():
    def __init__(self,
                 one_player_data
                 ):
        self.one_player = one_player_data
        self.completion_box = list()
        self.completion_interval = list()

    def get_completion_box(self):
        matrix = self.one_player
        for i in range(0, len(matrix)-1):
            if matrix[i+1][13:]!= matrix[i][13:]:
                self.completion_box.append(i+2)
        return self.completion_box

    def get_completion_interval(self, completion_box):
        for i in range(1,len(completion_box)):
            interval = completion_box[i] - completion_box[i-1]
            self.completion_interval.append(interval)
        self.completion_interval.insert(0,completion_box[0])
        return self.completion_interval






















