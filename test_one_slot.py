from collections import defaultdict
import random
import config
import draw_logic
from pprint import pprint
import convert_csv
import pool_selections as p


class BoxSimC():
    def __init__(self,fragments,logic,pool):
        self.fragments = fragments
        self.logic = logic
        self.pool = pool
        #self.inventory = defaultdict(int)
        #self.num_boxes = 0
        #self.result = defaultdict(list)
        self.get_reward()


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

    # def simulate_one_box(self):
    #     self.num_boxes += 1
    #     if self.has_reward():
    #         reward = self.get_reward()
    #         self.update_inventory(reward)
    #
    #     self.update_result(self.inventory)


    # FIXME, util function
    # def has_reward(self):
    #     if random.randint(1, 1):
    #         return True
    #     else:
    #         return False


    def get_reward(self):  #draw pieces from the pool
        reward = draw_logic.logic_factory(self.logic, self.pool).random_choice(pick=self.fragments)
        return reward


    # def update_inventory(self, reward):
    #     for hero_name in reward:
    #         self.inventory[hero_name] += 1
    #
    # def update_result(self, inventory):  #sort out reward, create hero,replace duplicates
    #     for hero_name, num_fragments in inventory.items():
    #         heroes = []
    #         for more_heroes in self.result.values():
    #             heroes += more_heroes
    #         if hero_name in heroes:
    #             continue
    #         else:
    #             if num_fragments == self.heroes[hero_name]:
    #                 self.result[self.num_boxes].append(hero_name)



    def get_result(self):
        return dict(self.result)



"""Put all slots together"""
def simulate_one_player():#simulate every draw, no create hero
    sim_1 = BoxSimC(config.c_fragments_per_slot,config.c_draw_logic_name,config.c_pool_name)

    result = []
    for num_boxes in range(1, 41): #FIXME stop condition
        slot_1 = sim_1.get_reward()

        result_all = (num_boxes, *slot_1)
        result.append(result_all)
    pprint(result)
    #convert_csv.output_csv_one_player(result)


# def main():
#     result = simulate(1)
#     print('result: ', result)

if __name__ == '__main__':
    simulate_one_player()