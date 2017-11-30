import simulator.output_handling
from simulator.pool_logic import *
from simulator.output_handling import OutputFormat
from simulator import config


def main():
    all_players_raw = []
    all_players_completion_box = []
    all_players_completion_interval = []
    all_trans_interval = []
    all_player_completion_names = []
    player_id = 1  # will be used for all data
    for i in range(0, config.player_num):
        sim = Simulation(config.a_fragments_per_slot,
                         config.slots_num,
                         config.pool_config.copy(),
                         config.prob_map.copy(),
                         config.prob_delta,
                         config.prob_delta_cap,
                         config.heroes)
        one_player = sim.run()
        completion_box = OutputFormat(one_player).get_completion_box()
        completion_interval = OutputFormat(one_player).get_completion_interval(completion_box)
        trans_interval = simulator.output_handling.transpose_interval(completion_interval)
        completion_interval.insert(0, player_id)
        completion_box.insert(0, player_id)
        one_player_completion_names = sim.inventory.completion
        one_player_completion_names.insert(0, player_id)
        # pprint(one_player_completion_names,width=200)

        for i in one_player:  # output full raw data matrix of all players
            i.insert(0, player_id)
        all_players_raw += one_player  # append complete data matrix
        all_players_completion_box.append(completion_box)  # output completion box for all players
        all_players_completion_interval.append(completion_interval)  # output completion interval for all players
        all_trans_interval += trans_interval
        all_player_completion_names.append(one_player_completion_names)
        player_id += 1  # update player_id

    simulator.output_handling.output_csv_all_players_completion_box(all_players_completion_box) # 1. write csv of all player, at which box an item is completed
    simulator.output_handling.output_csv_all_players_trans_interval(all_trans_interval)  # 2. write csv to transposed completion interval
    simulator.output_handling.output_csv_all_players_completion_names(all_player_completion_names)  # 3. write csv of the order of how each player complete the items
    simulator.output_handling.output_csv_all_players_completion_interval(all_players_completion_interval) # 4. write csv of completion interval
    simulator.output_handling.output_csv_all_players_raw(all_players_raw) # 5. write csv of raw data, a matrix of all players' inventory change and completion change


if __name__ == '__main__':
    main()
