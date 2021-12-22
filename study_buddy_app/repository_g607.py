import sqlite3
from datetime import datetime

database = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/study_buddy_app/database/study_buddy_g607.db"


def connect_to_database(path_to_database_file):
    conn = sqlite3.connect(path_to_database_file)
    return conn


def create_user(conn, body):
    query = """insert into users (first_name, last_name, email, password, faculty_id, created_at, updated_at)
    values (?, ?, ?, ?, ?, ?, ?)"""
    user_data = [
        body.get("first_name"),
        body.get("last_name"),
        body.get("email"),
        body.get("password"),
        body.get("faculty_id"),
        datetime.utcnow(),
        datetime.utcnow()
    ]
    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()


def get_username_and_password(conn, body):
    query = f"""select email, password from users where email='{body.get('email')}'"""
    cursor = conn.cursor()
    user = list(cursor.execute(query))
    if user:
        return user[0]
    else:
        return user
