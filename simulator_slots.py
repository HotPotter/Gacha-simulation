from collections import defaultdict
import random
import config
import draw_logic
from pprint import pprint
import convert_csv
import pool_selections as p


class BoxSimA():
    def __init__(self):
        self.heroes = config.heroes
        self.inventory = defaultdict(int)
        self.num_boxes = config.boxes_num
        self.completion = list()
        self.reward = list()
        self.pool = p.initial_1
        self.switch_count = 0

    def update_pool(self, completion): # FIXME, update pool, start with initial value read from config
        # for item in p.resource_initial:
        #     self.pool[item] = p.resource_all[item]

        for item in self.completion:
            try:
                self.pool[item]
                self.pool.pop(item)
                new_item_name = p.resource_expansion[self.switch_count]
                self.pool[new_item_name] = p.resource_all[new_item_name]
                self.switch_count +=1
            except:
                continue
        print("current pool:", self.pool) # Print current pool

        return self.pool
#



    # def simulate(self): # FIXME, 不同的停止条件
    #     self.simulate_until_pool_empty()

    # def simulate_n(self, n):
    #     for _ in range(n):
    #         self.simulate_one_box()
    #
    # def simulate_until_pool_empty(self):
    #     while True:
    #         self.simulate_one_box()
    #
    #         if len(self.hero_pool) == 0:
    #             break
    # def print_attri(self):
    #     print(self.num_boxes)
    #
    # def simulate_one_box(self):
    #     self.num_boxes += 1
    #     if self.has_reward():
    #         reward = self.get_reward()
    #         self.update_inventory(reward)
    #
    #     self.update_result(self.inventory)
    #     print("inventory:", self.inventory)


    # FIXME, util function
    def has_reward(self):
        if random.randint(1, 1):
            return True
        else:
            return False


    def get_reward(self, pool):  #draw pieces from the pool
        self.reward = draw_logic.logic_factory(config.a_draw_logic_name, self.pool).random_choice(pick=config.a_fragments_per_slot)
        print("reward is:", self.reward)
        return self.reward

    def update_inventory(self, reward):
        for val in reward:
            if val in self.inventory:
                self.inventory[val] += 1
            else:
                self.inventory[val] = 1
        return self.inventory

    def complete_item(self, inventory):  #sort out reward, create item,replace duplicates
        for item_name, num_fragments in self.inventory.items():
            if item_name in self.heroes.items():
                continue
            else:

                if num_fragments == self.heroes[item_name]:
                    self.completion.append(item_name)

            #items = []
            # for more_items in self.completion.values():
            #     items += more_items
            # if item_name in items:
            #     continue
            # else:
            #     if num_fragments == self.heroes[item_name]:
            #         self.completion[self.num_boxes].append(item_name)
        return self.completion



    def get_completion(self):
        return list(self.completion)

class BoxSimB():
    def __init__(self):
        self.heroes = config.heroes
        self.inventory = defaultdict(int)
        self.num_boxes = 0
        self.result = defaultdict(list)
        self.get_reward()


    def simulate_one_box(self):
        self.num_boxes += 1
        if self.has_reward():
            reward = self.get_reward()
            self.update_inventory(reward)

        self.update_result(self.inventory)

    # FIXME, util function
    def has_reward(self):
        if random.randint(1, 1):
            return True
        else:
            return False

    def get_reward(self):  # draw pieces from the pool
        reward = draw_logic.logic_factory(config.a_draw_logic_name, config.b_pool_name).random_choice(
            pick=config.b_fragments_per_slot)
        return reward

    def update_inventory(self, reward):
        for hero_name in reward:
            self.inventory[hero_name] += 1

    def update_result(self, inventory):  # sort out reward, create hero,replace duplicates
        for hero_name, num_fragments in inventory.items():
            heroes = []
            for more_heroes in self.result.values():
                heroes += more_heroes
            if hero_name in heroes:
                continue
            else:
                if num_fragments == self.heroes[hero_name]:
                    self.result[self.num_boxes].append(hero_name)

    def get_result(self):
        return dict(self.result)


"""Put all slots together"""
def simulate_one_player():#simulate every draw, no create hero
    sim_1 = BoxSimA()

    result = []

    for num_boxes in range(1, sim_1.num_boxes+1): #FIXME stop condition
        result_one_box = []
        for n in range(0, config.slots_num): # get the number of slots in the box
            slot_n=sim_1.get_reward(sim_1.pool)
            sim_1.update_inventory(slot_n)
            sim_1.complete_item(sim_1.inventory)
            sim_1.update_pool(sim_1.completion)
            #print('inventory:', *sim_1.inventory.items())
            print('completion:', sim_1.get_completion())
            result_one_box.append(*slot_n)
        result_all = (num_boxes, *result_one_box)
        result.append(result_all)
    pprint(result)
    #convert_csv.output_csv_one_player(result) # FIXME, need to adapt to slots number


# def main():
#     result = simulate(1)
#     print('result: ', result)

if __name__ == '__main__':
    simulate_one_player()