import sqlite3
from datetime import datetime


database = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/study_buddy_app/database/study_buddy_g611.db"


def connect_to_database(path_to_database_file):
    conn = sqlite3.connect(path_to_database_file)
    return conn


def create_user(conn, body):
    query = """insert into users(first_name, last_name, email, password, created_at, updated_at) 
    values (?,?,?,?,?,?)"""
    user_data = [
        body.get("first_name"),
        body.get("last_name"),
        body.get("email"),
        body.get("password"),
        datetime.utcnow(),
        datetime.utcnow()
    ]

    if user_data[0] == '' or user_data[1] == '' or user_data[2] == '' or user_data[3] == '':
        raise Exception("Missing user information.")

    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()


def get_email_and_password(conn, email):
    query = f"""select email, password from users where email='{email}'"""
    cursor = conn.cursor()
    user = list(cursor.execute(query))
    if user:
        return user[0]
    else:
        return user