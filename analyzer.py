# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import glob
import os

dictionary = {'Előzmények': 'date',
              'Testsúly (kg)' : 'weight',
              'Testmozgás (kcal)': 'burnt_calories',
              'Étel (kcal)': 'calorie_intake',
              'Zsír (g)' : 'fat',
              'Telített zsírok (g)' : 'saturated_fat',
              'Szénhídrátok (g)' : 'carbonhydrate',
              'Cukrok (g)' : 'sugar',
              'Fehérje (g)' : 'protein',
              'Élelmi rost (g)' : 'fiber',
              'Só (g)' : 'salt'}

def read_daily_data(path : str) -> pd.DataFrame:
    # TODO lot of distillation is needed for daily data
    temp_list = []
    all_files = glob.glob(path + r'\*.csv')
    for file_name in all_files:
        df = pd.read_csv(file_name)
        temp_list.append(df.T)

    return pd.concat(temp_list, axis=0)

def read_monthly_data(path : str) -> pd.DataFrame:
    temp_list = []
    all_files = glob.glob(path + r'\*.csv')

    for file_name in all_files:
        df = pd.read_csv(file_name)
        temp_list.append(df.T)

    return pd.concat(temp_list, axis=0, ignore_index=True)

if __name__ == '__main__':
    path_db= r'D:\Python_projects\health_analyzer\db'
    path_daily = os.path.join(path_db, 'daily')
    path_monthly = os.path.join(path_db, 'monthly')
    healthData = read_monthly_data(path_monthly)
    print(healthData.head())