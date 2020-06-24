def create_song_plays() -> str:
    """
    Dimension table
    :return:"""
    return """
    CREATE TABLE IF NOT EXISTS song_plays(
    id  SERIAL PRIMARY KEY, 
    start_time date REFERENCES time(start_time), 
    user_id int NOT NULL REFERENCES users(user_id), 
    level text, 
    song_id text REFERENCES songs(song_id), 
    artist_id text REFERENCES artists(artist_id), 
    session_id int, 
    location text, 
    user_agent text);
"""


def create_users() -> str:
    """
        Fact table
        :return:"""
    return """
    CREATE TABLE IF NOT EXISTS users (
    id  SERIAL PRIMARY KEY, 
    user_id int , 
    first_name text NOT NULL, 
    last_name text NOT NULL, 
    gender text, 
    level text);
"""


def create_songs() -> str:
    """
            Fact table
            :return:"""
    return """
    CREATE TABLE IF NOT EXISTS songs (
    id  SERIAL PRIMARY KEY, 
    song_id text, 
    title text NOT NULL, 
    artist_id text NOT NULL REFERENCES artists(artist_id), 
    year int, 
    duration float NOT NULL);
"""


def create_artists() -> str:
    """
            Fact table
            :return:"""
    return """
    CREATE TABLE IF NOT EXISTS artists(
    id  SERIAL PRIMARY KEY,
    artist_id text,
    name text NOT NULL, 
    location text, 
    lattitude float, 
    longitude float);
"""


def create_time() -> str:
    """
            Fact table
            :return:"""
    return """
    CREATE TABLE IF NOT EXISTS time( 
    id  SERIAL PRIMARY KEY,
    start_time date,
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday text);
"""
