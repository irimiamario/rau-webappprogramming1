import sqlite3


def connect_to_database(database_path):
    conn = sqlite3.connect(database_path)
    return conn 


def create_user(conn, data):
    query = "insert into users (first_name, last_name, email, password) values (?,?,?,?)"

    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
