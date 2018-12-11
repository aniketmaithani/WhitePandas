# -*- coding: utf-8 -*-
# @Author: aniketmaithani
# @Date:   2018-12-11 17:10:24
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2018-12-11 20:40:04

# Sort CSV file based on priority and time_to_expire field

import pandas as pd
from datetime import datetime


def sort_csv(file_name):
    # Pandas DataFrame
    df = pd.read_csv(file_name)
    df_sort_based_on_priority = df.sort_values('priority')
    df_sort_based_on_time = df_sort_based_on_priority.sort_values('time_to_expire')
    output_file = df_sort_based_on_time.to_csv('sorted_csv_file.csv', index=False)
    return output_file


def begin_from_time(time_args, filename):
    sort_csv(filename)
    df_for_parsed_date_field = pd.read_csv('sorted_csv_file.csv', parse_dates=[1])
    compared_time_args = datetime.strptime(time_args, '%Y-%m-%d %H:%M')
    result = df_for_parsed_date_field[df_for_parsed_date_field.time_to_expire >= compared_time_args]
    result.to_csv('final_result_execute.csv', index=False)
    return result
