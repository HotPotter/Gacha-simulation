class Fragment:
    def __init__(self,
                 name,
                 draw_probability,
                 fragments_required):
        self.name = name
        self.draw_probability = draw_probability
        self.fragments_required = fragments_required


class Hero(Fragment):
    def __init__(self, name, draw_probability, fragments_required):
        super().__init__(name, draw_probability, fragments_required)

    def __str__(self):
        return self.name


class Costume(Fragment):
    def __init__(self,
                 name,
                 draw_probability,
                 fragments_required,
                 of_hero,
                 ):
        super().__init__(name, draw_probability, fragments_required)

        self._of_hero = of_hero

    def __str__(self):
        return self.name
