import pandas as pd
import modules.database as db


def process_song_data(config: dict, file_path: str):
    data_frame = pd.read_json(file_path, lines=True)
    database_manager: db.DatabaseManager = db.DatabaseManager(config)
    artist = data_frame[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]
    artist.rename(columns={'artist_location': 'location',
                           "artist_latitude": "latitude",
                           "artist_longitude": "longitude"}, inplace=True)
    database_manager.df_insert(artist, "artists", "artist_id")
    song = data_frame[['song_id', 'title', 'artist_id', 'year', 'duration']]
    database_manager.df_insert(song, "songs", "song_id")
    database_manager.close_conn()
