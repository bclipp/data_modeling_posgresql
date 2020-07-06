import pandas as pd
import modules.data_base as db


def process_song_data(data_frame: pd.DataFrame, config: dict):
    database_manager: db.DatabaseManager = db.DatabaseManager(config)
    database_manager.df_insert(data_frame, "artists", "artist_id")
    database_manager.df_insert(data_frame, "songs", "song_id")
    database_manager.close_conn()
