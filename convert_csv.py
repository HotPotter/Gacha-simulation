"""output raw result data as csv file"""


import pandas as pd

def output_csv(result):
    data = pd.DataFrame(result)
    data.to_csv('csv_result.csv')

