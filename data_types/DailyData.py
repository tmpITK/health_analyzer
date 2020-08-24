import pandas as pd
from data_types.DataInterface import DataInterface

class DailyData(DataInterface):

    def __init__(self, df : pd.DataFrame, goal : pd.Series, date):
        super(DailyData, self).__init__(df, goal)
        self.date = date

    def __str__(self):
        return super(DailyData, self).__str__() + f'\nMonth:\n {self.date}'
