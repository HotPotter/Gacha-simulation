from simulator.fragments import Fragment, Hero, Costume


class Inventory:
    r"""
    :param initial_heroes: List of initial heroes
    :param initial_costumes: List of initial costumes
    :param
    """

    def __init__(self,
                 initial_heroes,
                 initial_costumes):
        self.completed_heroes = initial_costumes
        self.completed_costumes = initial_costumes

        self.collected_fragments = dict()
        self.event_buffer = list()

    def add_fragment_returns_is_completed(self, fragment):
        assert type(fragment) == Fragment

        self.event_buffer.append("Drew Fragment: {}".format(fragment.name))

        current_count_of_fragment = self.collected_fragments.get(fragment.name, 0)
        self.collected_fragments[fragment.name] = current_count_of_fragment + 1

        if self.collected_fragments[fragment.name] == fragment.fragments_required:
            if type(fragment) == Hero:
                self.completed_heroes.append(fragment.name)
                self.event_buffer.append("Created Hero: {}".format(fragment.name))

            if type(fragment) == Costume:
                self.completed_costumes.append(fragment.name)
                self.event_buffer.append("Created Costume: {}".format(fragment.name))
            else:
                raise NotImplementedError("Fragment type {} has not been implemented yet".format(type(fragment)))
            return True

        elif self.collected_fragments[fragment.name] > fragment.fragments_required:
            raise RuntimeError("The count of collected fragments should not be higher than the required fragments")

        else:
            return False

    def print_event_buffer(self):
        print(self.event_buffer)
