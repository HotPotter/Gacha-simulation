"""output raw result data as csv file"""


import pandas as pd


def output_csv_all_players(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result.csv')

def output_csv_one_player(result): # get only one player
    data = pd.DataFrame(result)
    data.to_csv('csv_result_one_player.csv', header=['box','slot1','slot2','slot3'], index=False)
    # data = pd.DataFrame(one_player)
    # data.to_csv('csv_result_one_player.csv')
