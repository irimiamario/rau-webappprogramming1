# pip install pysqlite3
import sqlite3


# connect to db --> connection object
def create_connection(dbfile):
    conn = sqlite3.connect(dbfile)
    return conn


# get a cursor --> cursor object
def create_cursor(conn):
    cursor = conn.cursor()
    return cursor


# run SQL commands using the cursor + connection object
# get all data inside the users table
def get_all_users(conn):
    query = "select * from users"
    cursor = conn.cursor()
    data = list(cursor.execute(query))
    return data


# insert one user
def insert_user(conn, user_data):
    query = """insert into users (username, first_name, last_name, email, password)
    values (?, ?, ?, ?, ?);"""
    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()


# get user email and pass
def get_user_email_and_pass(conn, username):
    query = f"""select username, email, password from users where username = '{username}'"""
    cursor = conn.cursor()
    results = list(cursor.execute(query))
    return results[0]


# delete
def delete_user(conn, user_id=None, username=None):
    query = ""
    if user_id is not None:
        query = f"delete from users where id = {user_id}"
    if username is not None:
        query = f"delete from users where username = '{username}'"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


# update
def update_user(conn, user_id=None, username=None, details=None):
    """
    UPDATE table_name
    SET column1 = value1, column2 = value2...., columnN = valueN
    WHERE [condition];

    details = {
    "email": "a@c.com"
    }
    """
    set_statement = ""
    for key, value in details.items():
        set_statement = set_statement + f"{key}={value},"
    set_statement = set_statement[:-1]
    query = ''
    if user_id is not None:
        query = f"update users set {set_statement} where id = {user_id}"
    if username is not None:
        query = f"update users set {set_statement} where username = '{username}'"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
