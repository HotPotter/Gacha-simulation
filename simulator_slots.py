from collections import defaultdict
import random
import config
import pool
from pprint import pprint

class BoxSim():
    def __init__(self):
        self.fragments_per_slot = config.fragments_per_slot
        self.heroes = config.heroes
        self.inventory = defaultdict(int)
        self.num_boxes = 0
        self.result = defaultdict(list)
        self.get_reward()
        #self.get_pool()

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

    def simulate_one_box(self):
        self.num_boxes += 1
        if self.has_reward():
            reward = self.get_reward()
            self.update_inventory(reward)

        self.update_result(self.inventory)

    # def get_pool(self): # pick and remove
    #     '''英雄奖池'''
    #     pool = []
    #     for hero_name, num in self.heroes.items():
    #         pool += [hero_name] * num
    #     random.shuffle(pool)
    #     self.hero_pool = pool

    # FIXME, util function
    def has_reward(self):
        if random.randint(0, 1):
            return True
        else:
            return False



    def get_reward(self):

        reward = pool.PoolFactory.create_pool(config.pool_name).random_choice(pick=self.fragments_per_slot)
        print('reward:', reward)
        return reward


    def update_inventory(self, reward):
        for hero_name in reward:
            self.inventory[hero_name] += 1

    def update_result(self, inventory):
        for hero_name, num_fragments in inventory.items():
            heroes = []
            for more_heroes in self.result.values():
                heroes += more_heroes
            if hero_name in heroes:
                continue
            else:
                if num_fragments == config.heroes[hero_name]:
                    self.result[self.num_boxes].append(hero_name)

    def get_result(self):
        return dict(self.result)

# def simulate(num_players):
#     result = []
#     for _ in range(num_players):
#         sim = HeroBoxSim()
#         #sim.simulate_until_pool_empty()
#         sim.simulate_n(12)
#         result.append(sim.get_result())
#     return result

def simulate_one_player():
    sim_1 = BoxSim()
    sim_2 = BoxSim()
    result = []
    for num_boxes in range(1, 20): #FIXME stop condition
        sim_1.simulate_one_box()
        slot_1 = sim_1.get_result()

        sim_2.simulate_one_box()
        slot_2 = sim_2.get_result()

        result_all = (num_boxes, slot_1, slot_2)
        result.append(result_all)
    #print('result: ', result)
    pprint(result)


# def main():
#     result = simulate(1)
#     print('result: ', result)

if __name__ == '__main__':
    simulate_one_player()