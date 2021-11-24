import sqlite3


def connect(db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        print("..SQLite connection established...")
    except Exception as e:
        print(f"--Failed to connect to {db_filename}. Error: {e}.")
        conn = None 
    return conn


def get_users(conn):
    query = "select * from users"
    try: 
        cursor = conn.cursor()
        results = list(cursor.execute(query))
        print("..Users returned successfully...")
        return results
    except Exception as e:
        print(f"--Failed to get all users. Error: {e}.")
        return []


def get_user_by_username(conn, username):
    query = f"select username, password from users where username='{username}'"
    try: 
        cursor = conn.cursor()
        user = list(cursor.execute(query))
        if len(user):
            user = user[0]
            result = {
                'username': user[0],
                'password': user[1]
            }
            print("..User returned successfully...")
            return result
    except Exception as e:
        print(f"--Failed to get user = {username}. Error: {e}.")
        return {}


def create_user(conn, user_details):
    value_keys = ",".join(user_details.keys())
    values = [user_details[k] for k, v in user_details.items()]
    n_values = ",".join(["?"] * len(values))
    query = f"insert into users ({value_keys}) values ({n_values})"
    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("..User created successfully...")
    except Exception as e:
        print(f"--Failed to insert new users. Error: {e}.")


def delete_user(conn, username):
    query = f"delete from users where username='{username}'"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("..User deleted successfully...")
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
        print("..User edited successfully...")
    except Exception as e:
        print(f"--Failed to update user details. Error: {e}.")


if __name__ == "__main__":
    """
    NOTE THAT I AM USING A DATABASE THAT DOESN'T HAVE THE FOLLOWING FIELDS:
    - created_at
    - last_updated_at
    - last_signed_in
    """
    conn = connect("user_management_api/db/users.db")
    users = get_users(conn)
    print(f"All users = {users}")
    new_user_details = {
        "username": "newusername",
        "first_name": "newuserfirstname",
        "last_name": "newuserlastname",
        "email": "newuser@email.com",
        "password": "3ri234pojfklnfjneh",
    }
    create_user(conn, user_details=new_user_details)
    new_user = get_user_by_username(conn, "newusername")
    print(f"Latest user created = {new_user}")
    new_user_changes = {
        "password": "23234324324234",
        "first_name": "newuserfirstname_updated"
    }
    edit_user(conn, "newusername", new_user_changes)
    edited_user = get_user_by_username(conn, "newusername")
    print(f"Latest user edited = {edited_user}")
    delete_user(conn, "newusername")

    
