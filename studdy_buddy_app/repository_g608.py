import sqlite3


DB_FILE = "/studdy_buddy_app/database/study_buddy_g608.db"


def connect_to_database(path_to_db_file):
    conn = sqlite3.connect(path_to_db_file)
    return conn


def create_user(conn, body):
    pass