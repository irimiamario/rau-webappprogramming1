import json
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


def get_user_profile(conn, user_id):
    # create query to extract data from db for user_id
    query = f"""select first_name, last_name, email, phone, year, knowledge, faculty.name as faculty_name from users 
    join faculty on users.faculty_id = faculty.id
    where users.id = {int(user_id)}"""

    # run query
    cursor = conn.cursor()
    user_details = list(cursor.execute(query))

    if len(user_details) == 0:
        return {}

    user_details = user_details[0]
    skills = []
    if user_details[5] is not None:
        skills = json.loads(user_details[5])

    profile = {
        "first_name": user_details[0],
        "last_name": user_details[1],
        "email": user_details[2],
        "phone": user_details[3],
        "year": user_details[4],
        "skills": skills,
        "faculty_name": user_details[6]
    }
    return profile


def update_user_profile(conn, user_details, user_id):
    # create update query
    set_statement = ''
    for key, value in user_details.items():
        if key in ["first_name", 'last_name', 'email', 'phone']:
            if value is not None:
                set_statement = set_statement + f"{key} = '{value}',"
            else:
                set_statement = set_statement + f"{key} = '',"

        if key == 'year':
            set_statement = set_statement + f"{key} = {value},"

        if key == 'skills':
            set_statement = set_statement + f"knowledge = '{json.dumps(value)}',"

    set_statement = set_statement[:-1]
    query = f"""UPDATE users SET {set_statement} WHERE id = {int(user_id)}"""

    # execute query
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


if __name__ == "__main__":
    conn = connect_to_database(DB_FILE)
    # password = get_user_password(conn, 'a@a.xyz')
    profile = get_user_profile(conn, 1)
    profile['year'] = 2022
    profile['phone'] = '+444444444'
    update_user_profile(conn, profile, 1)