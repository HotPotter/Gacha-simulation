from collections import defaultdict
import random
import config

class BoxSim():
    def __init__(self):
        self.fragments_per_box = config.fragments_per_box
        self.heroes = config.heroes
        self.inventory = defaultdict(int)
        self.num_boxes = 0
        self.result = defaultdict(list)
        self.make_hero_pool()

    def simulate(self): # FIXME, stop condition
        while True:
            self.num_boxes += 1
            if self.has_reward():
                reward = self.open_box()
                self.update_inventory(reward)

            self.update_result(self.inventory)

            if len(self.hero_pool) == 0:
                break
        pass

    def make_hero_pool(self):
        '''hero pool'''
        pool = []
        for hero_name, num in self.heroes.items():
            pool += [hero_name] * num
        random.shuffle(pool)
        self.hero_pool = pool

    # FIXME, util function
    def has_reward(self):
        if random.randint(0, 1):
            return True
        else:
            return False

    def update_inventory(self, reward):
        for hero_name in reward:
            self.inventory[hero_name] += 1

    def open_box(self):
        reward = self.hero_pool[0:self.fragments_per_box]
        self.hero_pool = self.hero_pool[self.fragments_per_box:]
        return reward

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

def simulate(num_players):
    result = []
    for _ in range(num_players):
        sim = BoxSim()
        sim.simulate()
        result.append(sim.get_result())
    return result

def main():
    result = simulate(1) #times of simulation
    print('result: ', result)

if __name__ == '__main__':
    main()