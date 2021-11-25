import sqlite3


def connect(dbfile):
    conn = sqlite3.connect(dbfile)
    return conn


def get_users(conn):
    query = "select * from users"
    cursor = conn.cursor()
    results = list(cursor.execute(query))
    return results


def get_user_by_username(conn, username):
    query = f"select username, password from users where username='{username}'"
    cursor = conn.cursor()
    raw_results = list(cursor.execute(query))
    if len(raw_results) == 1:
        results = {
            'username': raw_results[0][0],
            'password': raw_results[0][1]
        }
    else:
        results = {}
    return results


def push_user(conn, details):
    query = "insert into users (username, first_name, last_name, email, password) values (?, ?, ?, ?, ?)"
    user_data = [
        details["username"],
        details["first_name"],
        details["last_name"],
        details["email"],
        details["password"]
    ]
    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()


def delete_user(conn, username):
    query = f"delete from users where username='{username}'"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def edit_user(conn, username, details):
    """
    update users set
        username = 'usernamte1243',
        password = 'dlkdjfkljfgekrjflkd'
    where
        username = 'user1'
    """
    set_statement = ""
    for key, value in details.items():
        set_statement = set_statement + f"{key}='{value}',"
    set_statement = set_statement[:-1]

    query = f"update users set {set_statement} where username='{username}'"

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


if __name__ == "__main__":
    from pprint import pprint
    conn = connect("../user_management_api/db/users.db")
    print(conn)

    users = get_users(conn)
    pprint(users)

    user = get_user_by_username(conn, "username1")
    pprint(user)

    # new_user_details = {
    #     "username": "newusername_g610_4",
    #     "first_name": "newuserfirstname",
    #     "last_name": "newuserlastname",
    #     "email": "newuser_g610_4@email.com",
    #     "password": "fdkjflksjdf48375420349823rufh"
    # }
    # push_user(conn, details=new_user_details)
    user = get_user_by_username(conn, "newusername_g610_4")
    pprint(user)

    delete_user(conn, "liviu")
    users = get_users(conn)
    pprint(users)

    new_user_changes = {
        "password": "lfjkjfbnhjfsihfkhsf",
        "first_name": "newuserfirstname_updated_2"
    }
    edit_user(conn, "username1", new_user_changes)
    edited_user = get_user_by_username(conn, "username1")
    pprint(edited_user)