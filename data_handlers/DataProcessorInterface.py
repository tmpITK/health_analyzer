import pandas as pd
from typing import Type
import os
import json
from data_types.DataInterface import DataInterface
from abc import ABC, abstractmethod
from utils.io_ops import create_folder
import pickle

class DataPreprocessorInterface(ABC):

    def __init__(self,  db_path : str, sub_type : str):

        self.db_path = os.path.join(db_path, sub_type)
        self.dictionary_path = os.path.join(db_path, 'dictionary.json')
        with open(self.dictionary_path, encoding='utf-8') as f:
            self.dictionary = json.load(f)


    @abstractmethod
    def process_database(self) -> list:
        pass

    @abstractmethod
    def _clean_entry(self, df : pd.DataFrame) -> Type[DataInterface]:
        pass

    @abstractmethod
    def _extract_month(self, df : pd.DataFrame):
        pass

    def _save_clean_data(self, data : list):
        clean_data_path = os.path.join(self.db_path, 'clean')
        create_folder(clean_data_path)
        with open(os.path.join(clean_data_path, 'clean.pickle'), 'wb') as f:
            pickle.dump(data, f)

    def _translate_columns(self, df: pd.DataFrame):

        for col in df:
            for i, row in enumerate(df[col]):
                data_entry = df[col][i]

                if data_entry in self.dictionary:
                    print(data_entry)
                    df[col][i] = self.dictionary[data_entry]

                elif type(data_entry) == str and data_entry.replace('.','',1).isdigit():
                    df[col][i] = float(data_entry)

    def _extract_goal(self, df: pd.DataFrame) -> pd.DataFrame:
        goal_df = df.loc[df['date'] == 'goal']
        df = df[:-1]

        return df, goal_df

    def _convert_dates(self, df: pd.DataFrame):
        df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d').dt.date
        return df

    def _delete_only_nan_columns_and_rows(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.dropna(axis='rows', how='all')
        df = df.dropna(axis='columns', how='all')

        df.columns = df.iloc[0]
        df = df[1:]
        df.index = range(len(df))

        return df

    def _interpolate_missing_values(self, df: pd.DataFrame, columns : list, method='nearest', type_to_interpolate=float) -> pd.DataFrame:

        for col in columns:
            df[col] = df[col].astype(type_to_interpolate).interpolate(method=method)
            # last value is not interpolated
            df.loc[len(df[col]) - 1, col]= df.loc[len(df[col]) - 2, col]
        return df
