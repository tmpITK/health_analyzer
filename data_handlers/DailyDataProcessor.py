
import pandas as pd
from typing import Type
from data_handlers.DataProcessorInterface import DataPreprocessorInterface
from data_types.DataInterface import DataInterface
from data_types.DailyData import DailyData

class DailyDataProcessor(DataPreprocessorInterface):

    def __init__(self, db_path : str):
        super(DailyDataProcessor, self).__init__(db_path, 'daily')


    def _clean_entry(self, df : pd.DataFrame) -> Type[DataInterface]:
        self._translate_columns(df)

        return df
