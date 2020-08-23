from glob import glob
import pandas as pd
from typing import Type
from data_handlers.DataProcessorInterface import DataPreprocessorInterface
from data_types.DataInterface import DataInterface
from data_types.MonthlyData import MonthlyData

class MonthlyDataProcessor(DataPreprocessorInterface):

    def __init__(self, db_path : str):
        super(MonthlyDataProcessor, self).__init__(db_path, 'monthly')

    def process_database(self) -> list:

        data = []
        all_files = glob(self.db_path + r'\*.csv')

        for file_name in all_files:
            df = pd.read_csv(file_name)
            data.append(df)

        for index, raw_entry in enumerate(data):
            clean_entry = self._clean_entry(raw_entry)
            data[index] = clean_entry

        self._save_clean_data(data)

        return data

    def _clean_entry(self, df : pd.DataFrame) -> Type[DataInterface]:
        self._translate_columns(df)
        df = self._delete_only_nan_columns_and_rows(df)
        df = self._delete_missing_data_rows(df)
        df, goal = self._extract_goal(df)
        df = self._convert_dates(df)
        month = self._extract_month(df)

        return MonthlyData(df, goal, month)

    def _delete_missing_data_rows(self, df : pd.DataFrame) -> pd.DataFrame:

        df = df[df["calorie_intake"] != 0]
        df.index = range(len(df))
        return df

    def _extract_month(self, df : pd.DataFrame):
        arbitrary_date = df.date[0]
        return arbitrary_date.month