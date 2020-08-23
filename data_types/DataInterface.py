import pandas as pd
from abc import ABC

class DataInterface(ABC):

    def __init__(self, df : pd.DataFrame, goal : pd.Series):
        self.data = df
        self.goal = goal

    def __str__(self):

        return f"Data:\n {self.data}\n Goal:\n {self.goal}"


