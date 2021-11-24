import sqlite3


def connect(db_filename):
    try:
        conn = sqlite3.connect(db_filename)
    except Exception as e:
        print(f"--Failed to connect to {db_filename}. Error: {e}.")
        conn = None 
    return conn


def get_users(conn):
    query = "select * from users"
    try: 
        cursor = conn.cursor()
        results = list(cursor.execute(query))
    except Exception as e:
        print(f"--Failed to get all users. Error: {e}.")
        results = []
    return results


def get_user_by_username(conn, username):
    query = f"select username, password from users where username='{username}'"
    try: 
        cursor = conn.cursor()
        user = list(cursor.execute(query))
        if len(user):
            result = {
                'username': user[0],
                'password': user[1]
            }
            return result
    except Exception as e:
        print(f"--Failed to get all users. Error: {e}.")
        result = {}
    return result


def create_user(conn, user_details):
    value_keys = ",".join(user_details.keys())
    values = [user_details[k] for k, v in user_details.items()]
    n_values = ",".join(["?"] * (len(value_keys)-1))
    query = f"insert into users ({value_keys}) values ({n_values})"
    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print(f"--Failed to insert new users. Error: {e}.")


def delete_user(conn, username):
    query = f"delete from users where username='{username}'"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(f"--Failed to delete user = {username}. Error: {e}.")


def edit_user(conn, username, details):
    set_statement = ""
    for key, value in details.items():
        if type(value) == str:
            set_statement += f"{key}='{value}',"
        else:
            set_statement += f"{key}={value},"
    if len(set_statement) > 1:
        set_statement = set_statement[:-1]
    query = f"update users set {set_statement} where username='{username}'"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(f"--Failed to update user details. Error: {e}.")


if __name__ == "__main__":
    # run some tests to ensure everything works as expected
    create_user(None, {'a': 'b', 'c': 1})
    edit_user(None, 'abc', {'a': 'b', 'c': 1})
