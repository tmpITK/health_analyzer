import pandas as pd
from data_types.DataInterface import DataInterface

class MonthlyData(DataInterface):

    def __init__(self, df : pd.DataFrame, goal : pd.Series, month):
        super(MonthlyData, self).__init__(df, goal)
        self.month = month

    def __str__(self):
        return super(MonthlyData, self).__str__() + f'\nMonth:\n {self.month}'
