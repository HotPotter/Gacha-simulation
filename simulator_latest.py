from collections import defaultdict
import random
from pprint import pprint
import convert_csv
import config as c

class BoxSimA():
    def __init__(self,
                 heroes,
                 pool_list,
                 draw_probability_map,
                 pool_add,
                 completion_map,
                 inventory_map
                 ):
        self.heroes = heroes
        self.inventory = defaultdict(int) # FIXME this is the actual inventory dict
        self.inventory_map = inventory_map # FIXME this is for displaying the inventory for inventory_list
        self.completion = list()
        self.reward = list()
        self.pool_list = pool_list  # initial pool list
        self.draw_probability_map = draw_probability_map
        self.pool = defaultdict(int)
        self.pool_add = pool_add
        self.completion_map = completion_map

    def update_rate(self):  # update drop rate, apply delta
        delta = c.prob_delta
        for item in self.reward:  # FIXme, not likely to have more than 1 piece in a slot
            if self.draw_probability_map[item]< (c.resource_all[item]+ c.prob_delta_cap):
                self.draw_probability_map[item] += delta
        #pprint(self.draw_probability_map, width=300)
        return self.draw_probability_map

    def create_pool(self):  # create pool according to pool_list and probability map
        self.pool = defaultdict()
        try:
            for item in self.pool_list:
                self.pool[item] = self.draw_probability_map[item]
        except:
            raise ValueError('Your hand is empty!')
        return self.pool

    def update_pool_list(self):
        pool_add = self.pool_add
        for item in self.completion:
            if item in self.pool_list:
                self.pool_list.remove(item)
                if item == 'NUTCRACKER':
                    pool_add += c.resource_costume_nc
                random.shuffle(pool_add)
                if len(pool_add) > 0:
                    self.pool_list.append(pool_add.pop(0))
                else:  # when all items have been added into the pool
                    pass
            else:
                continue
        return self.pool_list

    def get_reward(self):  # draw pieces from the pool
        item_name = []
        item_prob = []
        try:
            pool_content = [item for item in self.pool.items()]
            for i, v in pool_content:
                item_name.append(i)
                item_prob.append(v)
            self.reward = random.choices(item_name, item_prob, k=c.a_fragments_per_slot)
        except Exception as e:
            print(e)
        return self.reward

    def update_inventory(self):
        for val in self.reward:
            if val in self.inventory:
                self.inventory[val] += 1
            else:
                self.inventory[val] = 1
        return self.inventory

    def complete_item(self):  # sort out reward, complete items if possible
        for item_name, num_fragments in self.inventory.items():
            if item_name in self.completion:
                continue
            else:

                if num_fragments == self.heroes[item_name]:
                    self.completion.append(item_name)

        return self.completion

    def get_completion(self):
        return list(self.completion)

    def update_completion_map(self):
        for i in self.completion_map:
            if i in self.completion:
                self.completion_map[i]=1
        return self.completion_map

    def update_inventory_map(self):
        for i in self.inventory_map:
            if i in self.inventory:
                self.inventory_map[i]= self.inventory[i]
        return self.inventory_map


def create_player(): # create instance from class
    player_x = BoxSimA(c.heroes.copy(),
                       c.resource_initial[:],
                       c.resource_all.copy(),
                       c.resource_expansion[:],
                       c.item_map.copy(),
                       c.inventory_map.copy())
    return player_x


def simulate_one_player(player_x):
    result_one_player = []
    num_boxes = 1
    while len(player_x.pool_list) > 0:  # FIXME stop condition, draw until pool is empty
        result_one_box = []
        for n in range(0, c.slots_num):  # get the number of slots in the box
            player_x.create_pool()
            slot_n = player_x.get_reward()
            player_x.update_rate()
            player_x.update_inventory()
            player_x.complete_item()
            player_x.update_pool_list()
            result_one_box.append(*slot_n)
        #print('inventory: ', player_x.inventory)
        inventory_dict = player_x.update_inventory_map()
        inventory_list = [v for i,v in inventory_dict.items()]
        #completion_dict = player_x.update_completion_map()
        #completion_list = [v for i,v in completion_dict.items()]
        #pprint(completion_list, width=300)
        result_all = (num_boxes, *result_one_box, *inventory_list) # *completion_list) > add completion map into the output
        result_one_player.append(result_all)
        num_boxes += 1

    return result_one_player

if __name__ == '__main__':
    all_players = []
    player_id = 0
    for i in range(1, c.player_num+1):
        player = create_player()
        result_one_player = simulate_one_player(player)
        result_one_player_l = [list(i) for i in result_one_player]
        for i in result_one_player_l:
            i.insert(0,player_id)
        all_players += result_one_player_l
        player_id+= 1
        #pprint(all_players)
        header = convert_csv.get_header()
        convert_csv.output_csv_all_players(i for i in all_players)
