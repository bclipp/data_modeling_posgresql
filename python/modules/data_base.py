import logging  # type: ignore
import pandas as pd  # type: ignore
import psycopg2  # type: ignore
import psycopg2.extras  # type: ignore
import modules.sql as sql


class DatabaseManager:

    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect_db(self):

        user = self.config["postgres_user"]
        password = self.config["postgres_password"]
        host = self.config["db_ip_address"]
        # port = self.config_dict["port"]
        database = self.config["postgres_db"]
        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            database=database,
            cursor_factory=psycopg2.extras.RealDictCursor
        )
        self.cursor = conn.cursor()
        self.conn = conn
        self.conn.autocommit = True

    def receive_sql_fetchall(self, sql_query: str) -> pd.DataFrame:

        try:
            self.cursor.execute(sql_query)
        except psycopg2.DatabaseError as error:
            logging.error(error)
            self.conn.rollback()
        return self.cursor.fetchall()

    def send_sql(self, sql_query: str) -> pd.DataFrame:

        try:
            self.cursor.execute(sql_query)
        except psycopg2.DatabaseError as error:
            logging.error(error)
            self.conn.rollback()

    def df_insert(self, data_frame: pd.DataFrame, table: str, conflict_id: str = None):

        try:
            if not data_frame.empty:
                data_frame_columns = list(data_frame)
                columns = ",".join(data_frame_columns)
                values = "VALUES({})".format(
                    ",".join(["%s" for _ in data_frame_columns])
                )
                if conflict_id:
                    insert_stmt = "INSERT INTO {} ({}) {} ON CONFLICT ({}) DO NOTHING;" \
                        .format(table,
                                columns,
                                values,
                                conflict_id)
                else:
                    insert_stmt = "INSERT INTO {} ({}) {};" \
                        .format(table,
                                columns,
                                values)
                psycopg2.extras.execute_batch(
                    self.cursor, insert_stmt, data_frame.values
                )
        except psycopg2.DatabaseError as error:
            logging.error(error)
            self.conn.rollback()

    def close_conn(self):

        self.cursor.close()

    def update_df(self, data_frame: pd.DataFrame, table: str):

        for i in range(len(data_frame)):
            row = data_frame.iloc[i]
            self.send_sql(sql.update_table(table, row))
