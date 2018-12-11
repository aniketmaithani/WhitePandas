import os
import sys
import pandas as pd
from datetime import datetime
from helper import begin_from_time
import time as dt


def execute_task(time_args, filename):
    begin_from_time(time_args, filename)
    df = pd.read_csv('final_result_execute.csv')
    df.time_to_expire = pd.to_datetime(df.time_to_expire)
    for time in df.time_to_expire:
        i = 0
        current_time = datetime.now()
        timedelta = time.to_pydatetime() - current_time
        if ((current_time == time.to_pydatetime()) and
                (timedelta.seconds) > 1):
            os.system(df.event_name[i] + "> /dev/null")
            print("Current Time {} , Event {} processed".format(
                time.to_pydatetime().strftime('%Y-%m-%d %H:%M'),
                df.event_name[i]))
            i = i + 1


if __name__ == "__main__":
    filename = sys.argv[1]
    date_args = sys.argv[2]
    time_args = sys.argv[3]
    date_time_args = '{} {}'.format(date_args, time_args)
    while 1:
        execute_task(date_time_args, filename)
        dt.sleep(5)
