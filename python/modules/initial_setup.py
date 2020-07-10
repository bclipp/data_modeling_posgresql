from modules import database as db, sql


def initialize_database(config: dict):
    if config["INIT"]:
        database_manager: db.DatabaseManager = db.DatabaseManager(config)
        database_manager.send_sql(sql.create_song_plays())
        database_manager.send_sql(sql.create_artists())
        database_manager.send_sql(sql.create_songs())
        database_manager.send_sql(sql.create_time())
        database_manager.send_sql(sql.create_users())
