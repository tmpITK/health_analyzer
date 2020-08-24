from glob import glob
import pandas as pd
from typing import Type
from data_handlers.DataProcessorInterface import DataPreprocessorInterface
from data_types.DataInterface import DataInterface
from data_types.MonthlyData import MonthlyData

class MonthlyDataProcessor(DataPreprocessorInterface):

    def __init__(self, db_path : str):
        super(MonthlyDataProcessor, self).__init__(db_path, 'monthly')

    def _clean_entry(self, df : pd.DataFrame) -> Type[DataInterface]:
        self._translate_columns(df)
        df = self._delete_only_nan_columns_and_rows(df)
        df = self._delete_missing_data_rows(df)
        df, goal = self._extract_goal(df)
        df = self._convert_dates(df)
        df = self._interpolate_missing_values(df, ['weight'])
        month = self._extract_month(df)

        return MonthlyData(df, goal, month)

    def _delete_missing_data_rows(self, df : pd.DataFrame) -> pd.DataFrame:

        df = df[df["calorie_intake"] != 0]
        df.index = range(len(df))
        return df

    def _extract_month(self, df : pd.DataFrame) -> str:
        arbitrary_date = df.date[0]
        return str(arbitrary_date.year - 2000) + str(arbitrary_date.month)