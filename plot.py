import matplotlib.pyplot as plt

'''Bar Chart'''
def my_plot(x, y):
    plt.bar(x, y, width=0.8, color='dodgerblue')
    plt.ylabel("Number of players")
    plt.xlabel("Get the first hero")
    plt.show()

