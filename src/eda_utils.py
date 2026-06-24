import matplotlib.pyplot as plt
import seaborn as sns


def plot_distribution(data, column):
    plt.figure(figsize=(8,5))
    sns.histplot(data[column], bins=40)
    plt.title(column)
    plt.show()