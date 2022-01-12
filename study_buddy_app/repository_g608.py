import sqlite3
from datetime import datetime

DB_FILE = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/study_buddy_app/database/study_buddy_g608.db"


def connect_to_database(path_to_db_file):
    conn = sqlite3.connect(path_to_db_file)
    return conn


def create_user(conn, body):
    # User details to insert:
    # first_name, last_name, email, password, created_at, updated_at

    # convert body from dict into a list or tuple
    user_details = [
        body.get("first_name", None),
        body.get("last_name", None),
        body.get("email", None),
        body.get("password", None),
        datetime.utcnow(),
        datetime.utcnow()
    ]

    if user_details[0] == '' or user_details[1] == '' or user_details[2] == '' or user_details[3] == '':
        raise Exception("Invalid user details provided.")

    # create query to insert new user into users table
    query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
    VALUES (?,?,?,?,?,?)"""

    # create a cursor
    cursor = conn.cursor()

    # use cursor to execute query
    cursor.execute(query, user_details)

    # commit changes to database using the connection (conn)
    conn.commit()


def get_user_password(conn, email):
    # create query to select user password for user with specified email
    query = f"""SELECT password FROM users WHERE email='{email}'"""

    # create a cursor to execute query
    cursor = conn.cursor()

    # execute query
    results = list(cursor.execute(query))

    # check if db returns an empty list. if yes, return None. else return value.
    if len(results) == 0:
        return None

    return results[0][0]


if __name__ == "__main__":
    conn = connect_to_database(DB_FILE)
    password = get_user_password(conn, 'a@a.xyz')
