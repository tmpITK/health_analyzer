# -*- coding: utf-8 -*-
from utils.constants import PATH_DB
from data_handlers.MonthlyDataProcessor import MonthlyDataProcessor
from data_handlers.DailyDataProcessor import DailyDataProcessor
from plotting.HealthPlotter import MonthlyPlotter
import pickle

if __name__ == '__main__':

    dp = MonthlyDataProcessor(PATH_DB)
    clean_data = dp.process_database()
    mp = MonthlyPlotter()

    #mp.plot_column(clean_data[0], columnToPlot='calorie_intake')
    #mp.plot_full_data(clean_data)
    mp.plot_feature_relationships(clean_data)
    mp.plot_correlations(clean_data)

    #testing
    with open(r'D:\Python_projects\health_analyzer\db\monthly\clean\clean.pickle', 'rb') as f:
        result = pickle.load(f)
        print(result[0])


    dp = DailyDataProcessor(PATH_DB)
    clean_data = dp.process_database()

    print(clean_data.head())
