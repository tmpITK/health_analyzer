# -*- coding: utf-8 -*-
from utils.constants import PATH_DB
from data_handlers.MonthlyDataProcessor import MonthlyDataProcessor
import pickle

if __name__ == '__main__':
    dp = MonthlyDataProcessor(PATH_DB)
    clean_data = dp.process_database()
    #testing
    with open(r'D:\Python_projects\health_analyzer\db\monthly\clean\clean.pickle', 'rb') as f:
        result = pickle.load(f)
        print(result[0])

