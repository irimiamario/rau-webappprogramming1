import sqlite3
from datetime import datetime

database = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/study_buddy_app/database/study_buddy_g612.db"


def connect_to_database(database_file):
    conn = sqlite3.connect(database_file)
    return conn


def create_user(conn, body):
    query = """insert into users(first_name, last_name, email, password, created_at, updated_at) 
    values (?, ?, ?, ?, ?, ?)"""
    user_data = [
        body.get("first_name"),
        body.get("last_name"),
        body.get("email"),
        body.get("password")
    ]
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()
    user_data.append(created_at)
    user_data.append(updated_at)

    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()


def get_user_password(conn, email):
    # creez query pentru a extrage parola utilizatorului din tabelul user
    query = f"""SELECT password FROM users WHERE email='{email}'"""

    # instantiez un cursor
    cursor = conn.cursor()

    # execut query folosind cursorul
    result = cursor.execute(query)
    result = list(result)

    # procesez rezultatul
    # daca rezultatul este o lista goala => return None
    if len(result) == 0:
        return None

    # daca rezultatul nu este o lista goala => return parola (elementul de pe pozitia 0 din prima intrare din lista cu
    # rezultate)
    return result[0][0]


if __name__ == "__main__":
    conn = connect_to_database(database)
    get_user_password(conn, 'al@a.com')