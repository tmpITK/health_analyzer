from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from mlxtend.plotting import scatterplotmatrix

class MonthlyPlotter:

    def __init__(self):
        pass

    def plot_column(self, df : pd.DataFrame, columnToPlot : str) -> None:

        x = [i for i in range(len(df.data.date))]
        y = df.data[columnToPlot].values
        plt.plot(x, y)
        plt.xticks(x, df.data.date, rotation=45)
        plt.ylabel(columnToPlot)
        plt.savefig(columnToPlot +'.png')
        plt.close()

    def plot_full_data(self, entries: list) -> None:
        num_rows = 3
        num_cols = 4
        for entry in entries:
            dates = entry.data.date
            x = [i for i in range(len(dates))]
            print(x)
            fig, axs = plt.subplots(3, 4, sharex=True)
            row_counter = 0
            col_counter = 0
            for col, value in entry.data.iteritems():
                if col == 'date':
                    continue
                axs[row_counter][col_counter].plot(x, value)
                axs[row_counter][col_counter].set_ylabel(str(col))
                axs[row_counter][col_counter].set_xticklabels(dates, rotation=45)
                row_counter = row_counter + 1 if row_counter < num_rows - 1 else 0
                col_counter = col_counter + 1 if col_counter < num_cols - 1 else 0

            axs[2][-1].set_xticklabels(dates, rotation=45)

            plt.show()

    def plot_feature_relationships(self, entries : list) -> None:

        for df in entries:
            cols = list(df.data.columns)
            scatterplotmatrix(df.data.values, names=cols, alpha=0.7)
            plt.savefig(f'feature_relationships_{df.month}')


