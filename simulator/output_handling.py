#print(header)

import pandas as pd

from simulator import config



header_raw = [i for i, v in config.heroes.items()]*2
header_raw.insert(0,'box id')
header_raw.insert(0,'player id')
header_completion_box = [i for i in range(1,len(config.heroes)+1)]
header_completion_box.insert(0, 'player id')

def output_csv_all_players_raw(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result_raw.csv',header=header_raw,index=False)


def output_csv_all_players_completion_box(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result_comp_box.csv',header=None,index=False)


def output_csv_all_players_completion_interval(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result_comp_interval.csv',header=None,index=False)


def output_csv_all_players_trans_interval(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result_trans_interval.csv', header=['interval'], index=False)


def output_csv_all_players_completion_names(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result_completion_names.csv', header=None, index=False)


def transpose_interval(interval):
    diff_array = []
    for i in interval:
        li = [i]
        diff_array.append(li)
    return diff_array





class OutputFormat():
    def __init__(self,
                 one_player_data
                 ):
        self.one_player = one_player_data
        self.completion_box = list()
        self.completion_interval = list()

    def get_completion_box(self):
        matrix = self.one_player
        for i in range(0, len(matrix)-1):
            if matrix[i+1][13:]!= matrix[i][13:]:
                self.completion_box.append(i+2)
        return self.completion_box

    def get_completion_interval(self, completion_box):
        for i in range(1,len(completion_box)):
            interval = completion_box[i] - completion_box[i-1]
            self.completion_interval.append(interval)
        self.completion_interval.insert(0,completion_box[0])
        return self.completion_interval
