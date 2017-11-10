from collections import defaultdict
import random
import config
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
        self.pool_list = p.resource_initial  # initial pool list
        self.rate = p.resource_all
        self.pool = defaultdict(int)
        self.switch_count = 0

    def update_rate(self):  # update drop rate, apply delta
        delta = config.prob_delta
        for item in self.reward:
            self.rate[item] += delta
        return self.rate

    def create_pool(self):
        # print('current pool list', self.pool_list)
        self.pool = defaultdict()
        try:
            for item in self.pool_list:
                self.pool[item] = self.rate[item]
        except:
            raise ValueError('Your hand is empty!')
        return self.pool

    def update_pool_list(self):  # FIXME, update pool, start with initial value read from config
        pool_add = p.resource_expansion
        for item in self.completion:
            if item in self.pool_list:
                self.pool_list.remove(item)
                if item == 'NUTCRACKER':
                    pool_add += p.resource_costume_nc
                else:
                    pass
                random.shuffle(pool_add)
                if len(pool_add) > 0:
                    self.pool_list.append(pool_add.pop(0))
                else:
                    print('yoo')
                # except:
                #     print('no new item')

            else:
                continue
        # print('current pool list:', self.pool_list)
        return self.pool_list


    def get_reward(self):  # draw pieces from the pool
        item_name = []
        item_prob = []
        try:
            pool_content = [item for item in self.pool.items()]
            for i, v in pool_content:
                item_name.append(i)
                item_prob.append(v)
            self.reward = random.choices(item_name, item_prob, k=config.a_fragments_per_slot)
        except Exception as e:
            print(e)

        # self.reward = draw_logic.logic_factory(config.a_draw_logic_name, self.pool).random_choice(
        #     pick=config.a_fragments_per_slot)
        # print("reward is:", self.reward)
        return self.reward

    def update_inventory(self):
        for val in self.reward:
            if val in self.inventory:
                self.inventory[val] += 1
            else:
                self.inventory[val] = 1
        return self.inventory

    def complete_item(self):  # sort out reward, create item,replace duplicates
        for item_name, num_fragments in self.inventory.items():
            if item_name in self.completion:
                continue
            else:

                if num_fragments == self.heroes[item_name]:
                    self.completion.append(item_name)

        return self.completion

    def get_completion(self):
        return list(self.completion)


"""Put all slots together"""


def simulate_one_player():  # simulate every draw, no create hero
    sim_1 = BoxSimA()
    result = []
    # sim_1.pool_list = p.resource_initial # initiate the pool
    for num_boxes in range(1, sim_1.num_boxes + 1):  # FIXME stop condition
        result_one_box = []
        for n in range(0, config.slots_num):  # get the number of slots in the box
            sim_1.create_pool()
            # print('start pool:', sim_1.pool)
            slot_n = sim_1.get_reward()
            # print("reward is:", slot_n)
            sim_1.update_rate()
            sim_1.update_inventory()
            sim_1.complete_item()
            sim_1.update_pool_list()
            # print('updated pool list', sim_1.pool_list)
            # print('end')
            result_one_box.append(*slot_n)
        result_all = (num_boxes, *result_one_box)
        result.append(result_all)
    pprint(result)
    # convert_csv.output_csv_one_player(result) # FIXME, need to adapt to slots number


# def main():
#     result = simulate(1)
#     print('result: ', result)

if __name__ == '__main__':
    simulate_one_player()
