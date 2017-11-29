import unittest

from simulator.objects import *

# class TestDrawFromBox(unittest.TestCase):
#     def test_returns_correct_draw(self):
#         a_draw = DrawFromBox(1,1,
#                              {"NUTCRACKER": 10,
#                               "t1": 1,
#                               "y1": 1,
#                               "t2": 1})
#         actual = a_draw.get_reward()
#         should_be = ['NUTCRACKER']
#         self.assertListEqual(actual,should_be)

# class TestPool(unittest.TestCase):
#     def test_returns_correct_updated_pool_list(self):
#         item_config = ItemConfig({"NUTCRACKER": 10,
#                                       "t1": 10,
#                                       "y1": 10,
#                                       "t2": 10,
#                                       "MISTY": 10,
#                                       "ODUS": 10,
#                                       "t3": 10,
#                                       "y2": 10,
#                                       "y3": 10,
#                                       "n1": 10,
#                                       "n2": 10,
#                                       "n3": 10},
#                                      {"NUTCRACKER": 1,
#                                       "t1": 0,
#                                       "y1": 0,
#                                       "t2": 0,
#                                       "MISTY": 1,
#                                       "ODUS": 1,
#                                       "t3": 0,
#                                       "y2": 0,
#                                       "y3": 0,
#                                       "n1": 0,
#                                       "n2": 0,
#                                       "n3": 0})
#         inventory = Inventory(item_config)
#         inventory.completion = ['NUTCRACKER', 'MISTY','ODUS']
#         pool = Pool({"NUTCRACKER": 1,
#                      "t1": 0,
#                      "y1": 0,
#                      "t2": 0,
#                      "MISTY": 1,
#                      "ODUS": 1,
#                      "t3": 0,
#                      "y2": 0,
#                      "y3": 0,
#                      "n1": 0,
#                      "n2": 0,
#                      "n3": 0},
#                     {"NUTCRACKER": 10,
#                      "t1": 10,
#                      "y1": 10,
#                      "t2": 10,
#                      "MISTY": 10,
#                      "ODUS": 10,
#                      "t3": 10,
#                      "y2": 10,
#                      "y3": 10,
#                      "n1": 10,
#                      "n2": 10,
#                      "n3": 10},
#                     1,
#                     10,
#                     inventory)
#         pool.update_pool()
#         actual = pool.pool_list
#         should_be = ['MISTY','ODUS']
#         self.assertListEqual(actual,should_be)

    # def test_returns_correct_pool(self):
    #     pool = Pool({"NUTCRACKER": 1,
    #                  "t1": 0,
    #                  "y1": 0,
    #                  "t2": 0,
    #                  "MISTY": 1,
    #                  "ODUS": 1,
    #                  "t3": 0,
    #                  "y2": 0,
    #                  "y3": 0,
    #                  "n1": 0,
    #                  "n2": 0,
    #                  "n3": 0},
    #                 {"NUTCRACKER": 10,
    #                  "t1": 10,
    #                  "y1": 10,
    #                  "t2": 10,
    #                  "MISTY": 10,
    #                  "ODUS": 10,
    #                  "t3": 10,
    #                  "y2": 10,
    #                  "y3": 10,
    #                  "n1": 10,
    #                  "n2": 10,
    #                  "n3": 10},
    #                 config.prob_delta,
    #                 config.prob_delta_cap,
    #                 {'NUTCRACKER', 1})
    #     actual = pool.pool
    #     should_be = {"NUTCRACKER": 10,
    #                  "MISTY": 10,
    #                  "ODUS": 10}
    #     self.assertDictEqual(actual, should_be)

        # def test_update_correct_prob_map(self):
        #     pool = Pool(['NUTCRACKER', 't1', 'y1', 't2','y3','t3'],
        #                 {"NUTCRACKER": 10,
        #                  "t1": 10,
        #                  "y1": 10,
        #                  "t2": 10,
        #                  "MISTY": 10,
        #                  "ODUS": 10,
        #                  "t3": 10,
        #                  "y2": 10,
        #                  "y3": 10,
        #                  "n1": 10,
        #                  "n2": 10,
        #                  "n3": 10},
        #                 config.prob_delta,
        #                 config.prob_delta_cap,
        #                 {'NUTCRACKER':1})
        #
        #     self.assertDictEqual(pool.renew_prob(), {"NUTCRACKER": 11,
        #                  "t1": 10,
        #                  "y1": 10,
        #                  "t2": 10,
        #                  "MISTY": 10,
        #                  "ODUS": 10,
        #                  "t3": 10,
        #                  "y2": 10,
        #                  "y3": 10,
        #                  "n1": 10,
        #                  "n2": 10,
        #                  "n3": 10} )

class TestInventory(unittest.TestCase):
    # def test_create_correct_completion(self):
    #     item_config = ItemConfig({"NUTCRACKER": 10,
    #                  "t1": 10,
    #                  "y1": 10,
    #                  "t2": 10},
    #                 {"NUTCRACKER": 0,
    #                  "t1": 0,
    #                  "y1": 0,
    #                  "t2": 0})
    #     inventory = Inventory(item_config)
    #     inventory.inventory = {"NUTCRACKER": 0,
    #                  "t1": 0,
    #                  "y1": 0,
    #                  "t2": 10}
    #     self.assertListEqual(inventory.get_completion(),['t2'])

    def test_update_inventory(self):
        test_inventory = Inventory ({"NUTCRACKER": 1,
                     "t1": 1,
                     "y1": 1,
                     "t2": 1})
        test_inventory.update(['t1'])
        actual = test_inventory.inventory
        should_be = {"t1": 1}
        self.assertDictEqual(actual,should_be)
