import sqlite3


def connect(dbfile):
    try:
        # connect to dbfile using sqlite3
        conn = sqlite3.connect(dbfile)
        # return connection object
        return conn
    except Exception as e:
        # create an error (optional)
        # log error (optional)
        # raise error
        raise e


def create_user(conn, details):
    # create insert query
    query = "insert into users (first_name, last_name, email, password) values (?,?,?,?)"

    # create a cursor using conn
    cursor = conn.cursor()

    # use cursor to execute query
    cursor.execute(query, details)

    # commit insert using conn
    conn.commit()