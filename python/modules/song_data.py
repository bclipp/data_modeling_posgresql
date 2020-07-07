import pandas as pd
import modules.database as db


def process_song_data(file_path: str):
    data_frame = pd.read_json(file_path, lines=True)
    database_manager: db.DatabaseManager = db.DatabaseManager(config)
    database_manager.df_insert(data_frame, "artists", "artist_id")
    database_manager.df_insert(data_frame, "songs", "song_id")
    database_manager.close_conn()
