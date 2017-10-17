import matplotlib.pyplot as plt

'''Bar Chart - using list'''
def plot_bar_list(x, y):
    plt.bar(x, y, width=0.8, color='dodgerblue')
    plt.ylabel("Number of players")
    plt.xlabel("Get the first hero")
    plt.show()

'''Bar Chart - using dictionary'''

def plot_bar_dict(d):
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), d.keys())
    plt.ylabel("Number of players")
    plt.xlabel("Get the first hero")
    plt.show()