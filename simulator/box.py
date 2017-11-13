class Box:
    def __init__(self,
                 draw_probability_map,
                 initial_fragments_pool,
                 extension_fragments,
                 number_of_slots):

        self._draw_probability_map = draw_probability_map
        self._current_fragment_pool = initial_fragments_pool
        self._extension_fragments = extension_fragments
        self._number_of_slots = number_of_slots


    def draw(self, inventory):
        pass