import pandas as pd

def output_csv(result):
    data = pd.DataFrame(result)
    print(data)
    data.to_csv('csv_output.csv')

# result = [{7: ['kimmy'], 8: ['yeti'], 9: ['toffee', 'troll', 'tiffy']},{7: ['troll'], 8: ['tiffy'], 9: ['toffee', 'yeti', 'kimmy']},{6: ['yeti'], 8: ['tiffy'], 9: ['troll', 'toffee', 'kimmy']}]
#
# data = pd.DataFrame(result)
#
# print(data)
#
# data.to_csv('csv_output.csv')

# with open('csv_output.csv', 'w') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(data)
#     # for i in data:
#     #     print(i)
#     #     wr.writerow(i)
