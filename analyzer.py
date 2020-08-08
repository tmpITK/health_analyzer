import pandas as pd
import numpy as np
import glob

def read_data(path):
    temp_list = []
    all_files = glob.glob(path + r'\*.csv')
    for file_name in all_files:
        df = pd.read_csv(file_name)
        temp_list.append(df.T)

    return pd.concat(temp_list, axis=0, ignore_index=True)

if __name__ == '__main__':
    path = r'D:\Python_projects\health_analyzer\db'
    raw_dataFrame = read_data(path)
    print(raw_dataFrame.head())