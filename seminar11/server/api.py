from flask import Flask, request
from flask_cors import CORS

from seminar11.database.repository import connect, create_user, get_email_and_password

app = Flask("MyFirstUserManagementApp")
CORS(app)

DB_FILE = '../database/basic_users.db'


@app.route('/api/v1/users', methods=["POST"])
def users():
    user_details = request.json
    password = user_details.get("password", None)
    second_password = user_details.get("secondPassword", None)
    if password != second_password:
        error = {
            "error": "--Failed to create users. Passwords don't match."
        }
        return error, 400

    try:
        conn = connect(DB_FILE)
        details = {
            "first_name": user_details.get("firstName", None),
            "last_name": user_details.get("lastName", None),
            "email": user_details.get("email", None),
            "password": user_details.get("password", None)
        }
        create_user(conn, details)
        conn.close()
        return '', 200
    except Exception as e:
        error = {
            'error': {e}
        }
        return error, 500


@app.route('/api/v1/users/<email>', methods=["GET"])
def get_user(email):
    if email is None:
        error = {
            "error": "--Invalid email provided."
        }
        return error, 400

    try:
        conn = connect(DB_FILE)
        user = get_email_and_password(conn, email)
        response = {
            "user": user
        }
        return response, 200
    except Exception as e:
        error = {
            "error": f"--Failed to fetch user. {e}"
        }
        return error, 500


@app.route('/api/v1/sign-in', methods=["POST"])
def sign_in():
    body = request.json
    email = body.get("email", None)
    password = body.get("password", None)
    if email is None:
        error = {
            "error": "--Please provide an email."
        }
        return error, 400

    if password is None:
        error = {
            "error": "--Please provide a password."
        }
        return error, 400

    # sign in
    try:
        conn = connect(DB_FILE)
        user = get_email_and_password(conn, email)
        if user and user["password"] == password:
            return '', 204
        else:
            error = {
                "error": "--Failed to sign-in. Email or password are invalid."
            }
            return error, 401
    except Exception as e:
        error = {
            "error": f"--Failed to sign-in. {e}"
        }
        return error, 500


if __name__ == "__main__":
    app.run(port=3002, debug=True)
