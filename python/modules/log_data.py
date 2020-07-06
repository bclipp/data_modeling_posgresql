import pandas as pd
import modules.data_base as db


def process_log_data(data_frame: pd.DataFrame, config: dict):
    data_frame = data_frame[data_frame['page'] == "NextSong"]
    data_frame["ts"] = data_frame['ts'].astype({'ts': 'datetime64[ms]'})
    time_stamps: pd.Series = pd.Series(data_frame['ts'], index=data_frame.index)
    time_data = []
    for time_stamp in time_stamps:
        time_data.append([time_stamp,
                          time_stamp.hour,
                          time_stamp.day,
                          time_stamp.weekofyear,
                          time_stamp.month,
                          time_stamp.year,
                          time_stamp.day_name()])

    column_labels = ('start_time', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday')
    time: pd.DataFrame = pd.DataFrame.from_records(data=time_data, columns=column_labels)
    database_manager: db.DatabaseManager = db.DatabaseManager(config)
    database_manager.df_insert(time, "time")
    user = data_frame[['userId', 'firstName', 'lastName', 'gender', 'level']]
    database_manager.df_insert(user, "users")
    # songplay
