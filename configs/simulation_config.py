
"""
BoxSimA configuration - USER INPUT
"""
a_fragments_per_slot = 1
slots_num = 3  # number of slots in the box
boxes_num = 30  # number of boxes to open
prob_delta = 20  # probability change after each draw



"""
Draw probability of each fragment
"""
draw_probability_map = {"NUTCRACKER": 10,
                "T1": 1,
                "Y1": 1,
                "T2": 1,
                "MISTY": 1,
                "ODUS": 1,
                "T3": 1,
                "Y2": 1,
                "Y3": 1,
                "N1": 1,
                "N2": 1,
                "N3": 1}

"""
Heroes and costumes that are in the initial draw Pool of the Loot Boxes
"""
initial_heroes_draw_pool = ['NUTCRACKER']
initial_costumes_draw_pool = ['T1', 'Y1', 'T2']

"""
Heroes and costumes that replace items in the draw pool, where all fragments 
have been collected
"""
extension_heroes_draw_pool = ['MISTY', 'ODUS']
extension_costumes_draw_pool = ['T3','Y2', 'Y3', 'N1', 'N2', 'N3']

"""
Inventory of heroes and costumes, with which the player starts
"""
initial_heroes_inventory = ['TIFFY', 'YETI']
initial_costumes_inventory = []
