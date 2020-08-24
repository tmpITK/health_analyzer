from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from mlxtend.plotting import scatterplotmatrix, heatmap

class MonthlyPlotter:

    def __init__(self):
        pass

    def plot_column(self, df : pd.DataFrame, columnToPlot : str) -> None:

        x = [i for i in range(len(df.date))]
        y = df[columnToPlot].values
        plt.plot(x, y)
        plt.xticks(x, df.date, rotation=45)
        plt.ylabel(columnToPlot)
        plt.savefig(columnToPlot +'.png')
        plt.close()

    def plot_full_data(self, df : pd.DataFrame) -> None:
        num_rows = 3
        num_cols = 4

        dates = df.date
        x = [i for i in range(len(dates))]
        print(x)
        fig, axs = plt.subplots(3, 4, sharex=True)
        row_counter = 0
        col_counter = 0
        for col, value in df.iteritems():
            if col == 'date':
                continue
            axs[row_counter][col_counter].plot(x, value)
            axs[row_counter][col_counter].set_ylabel(str(col))
            axs[row_counter][col_counter].set_xticklabels(dates, rotation=45)
            row_counter = row_counter + 1 if row_counter < num_rows - 1 else 0
            col_counter = col_counter + 1 if col_counter < num_cols - 1 else 0

        axs[2][-1].set_xticklabels(dates, rotation=45)

        plt.show()

    def plot_feature_relationships(self, df : pd.DataFrame, cols=[], postfix='') -> None:

        no_date_df = df.drop(columns=['date'])

        if not cols:
            cols = list(no_date_df.columns)

        scatterplotmatrix(no_date_df.values, names=cols, alpha=0.7)
        plt.savefig(f'feature_relationships{postfix}.png')

    def plot_correlations(self, df : pd.DataFrame, cols=[], postfix='') -> None:

        no_date_df = df.drop(columns=['date'])

        if not cols:
            cols = list(no_date_df.columns)

        corr = np.corrcoef(no_date_df[cols].values.T)
        heat = heatmap(corr, row_names=cols, column_names=cols)
        plt.show()
        plt.savefig(f'correlation_matrix{postfix}.png')


