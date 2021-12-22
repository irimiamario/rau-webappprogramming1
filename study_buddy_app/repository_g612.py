import sqlite3
from datetime import datetime

database = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/study_buddy_app/database/study_buddy_g612.db"


def connect_to_database(database_file):
    conn = sqlite3.connect(database_file)
    return conn


def create_user(conn, body):
    query = """insert into users(first_name, last_name, email, password, faculty_id, created_at, updated_at) 
    values (?, ?, ?, ?, ?, ?, ?)"""
    user_data = [
        body.get("first_name"),
        body.get("last_name"),
        body.get("email"),
        body.get("password"),
        body.get("faculty_id"),
    ]
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()
    user_data.append(created_at)
    user_data.append(updated_at)

    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()
