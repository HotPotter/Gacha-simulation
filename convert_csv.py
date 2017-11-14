import pandas as pd
import config

def get_header():
    header_start = ['player id','box']
    header_end = [i for i in config.inventory_map]
    for i in range(1, config.slots_num+1):
        slot = ['slot%s'%i]
        header_start += slot
    header = header_start + header_end
    return header


def output_csv_all_players(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result.csv',header=get_header(),index=False)


