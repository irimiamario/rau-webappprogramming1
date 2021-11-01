import sqlite3
from sqlite3 import Error
import json 

from flask import Flask, Response
from flask_restful import Api, Resource, request

def create_connection(db_filename):
    conn = None
    try:
        conn = sqlite3.connect(db_filename)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


"""
CREATE TABLE IF NOT EXISTS companies (
    id integer PRIMARY KEY,
    name text NOT NULL,
);

CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL, 
    password text NOT NULL,
    company_id integer NOT NULL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
"""

def create_company(conn, company):
    query = """INSERT INTO companies(name)
    VALUES(?)"""
    cur = conn.cursor()
    cur.execute(query, company)
    conn.commit()
    return cur.lastrowid

def create_user(conn, user):
    query = """INSERT INTO users(name, email, password, company_id)
    VALUES(?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(query, user)
    conn.commit()
    return cur.lastrowid

def get_users(conn):
    query = """SELECT * FROM users"""
    cur = conn.cursor()
    results = cur.execute(query)
    return list(results) 

def get_username_and_email(conn):
    query = "SELECT name, email FROM users"
    cur = conn.cursor()
    results = cur.execute(query)
    return list(results)

def username(users):
    for user in users:
        print(f"Username: {user[1]}")


app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self, id=None):
        conn = create_connection("seminar9/users.db")
        if id is None:
            try:
                users = get_username_and_email(conn)
                users_json = json.dumps(users)
                response = Response(response=users_json, status=200, content_type="application/json")
            except Exception as e:
                conn.close()
                response = Response('{"error": "Failed to get all users"}', status=500, content_type="application/json")    
        conn.close()
        return response 
        
    def post(self):
        conn = create_connection("seminar9/users.db")
        data = request.json
        user = (data['name'], data['email'], data['password'], data['company_id'])
        try:
            create_user(conn, user)
            response = Response(status=200, content_type="application/json")
        except:
            response = Response('{"error": "Failed to get create user"}', status=500, content_type="application/json")
        conn.close()
        return response 

class Company(Resource): 
    def get(self, name):
        pass 

    def post(self):
        conn = create_connection("seminar9/users.db")
        data = request.json 
        company = (data['name'], )
        try: 
            create_company(conn, company)
            response = Response(status=200, content_type="application/json")
        except:
            response = Response('{"error": "Failed to get create company"}', status=500, content_type="application/json")
        conn.close()
        return response 

api.add_resource(User, '/users', '/users/<string:id>')
api.add_resource(Company, '/companies')

if __name__ == "__main__":
    # create_companies_table = """CREATE TABLE IF NOT EXISTS companies (
    # id integer PRIMARY KEY,
    # name text NOT NULL);
    # """

    # create_users_table = """CREATE TABLE IF NOT EXISTS users (
    # id integer PRIMARY KEY,
    # name text NOT NULL,
    # email text NOT NULL, 
    # password text NOT NULL,
    # company_id integer NOT NULL,
    # FOREIGN KEY (company_id) REFERENCES companies(id));
    # """

    # # create connection 
    # conn = create_connection("seminar9/users.db")

    # # create tables if they don't exist already
    # create_table(conn, create_companies_table)
    # create_table(conn, create_users_table)

    # # # insert a company
    # # company = ('Company 1',)
    # # company_id = create_company(conn, company)

    # # # insert new users
    # # user1 = ('User 1 Full Name', 'user1@company.com', 'password1234', company_id)
    # # user2 = ('User 2 Full Name', 'user2@company.com', 'password12345', company_id)

    # # user1_id = create_user(conn, user1)
    # # user2_id = create_user(conn, user2)

    # # print(f"Created the following users {[user1_id, user2_id]}")

    # # get all users
    # users = get_users(conn)
    # username(users)

    # # get user and email
    # r = get_username_and_email(conn)
    # print(r)
    # conn.close()

    app.run(debug=True)