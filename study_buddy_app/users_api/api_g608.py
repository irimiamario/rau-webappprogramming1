from flask import Flask, request
from flask_cors import CORS

from study_buddy_app.repository_g608 import DB_FILE, get_user_password
from study_buddy_app.repository_g608 import connect_to_database, create_user

app = Flask("UsersAPI")
CORS(app)


@app.route("/api/v1/signup", methods=["POST"])
def signup():
    body = request.json
    try:
        conn = connect_to_database(DB_FILE)
        create_user(conn, body)
        conn.close()
        return '', 200
    except Exception as e:
        error = {
            "error": f"--Failed to create user. Message {e}"
        }
        return error, 500


@app.route("/api/v1/sign-in", methods=["POST"])
def sign_in():
    # extract request body
    body = request.json

    # get email from body
    email = body.get("email", None)
    if email is None:
        error = {
            "error": "--Failed to sign in. Missing username."
        }
        return error, 400

    # get password from body
    password = body.get("password", None)
    if password is None:
        error = {
            "error": "--Failed to sign in. Missing password."
        }
        return error, 400

    # get user password from our database
    try:
        conn = connect_to_database(DB_FILE)
        existing_password = get_user_password(conn, email)
    except Exception as e:
        error = {
            "error": f"--Failed to sign in. Message: {e}"
        }
        return error, 500

    # check if user password exists. if it doesn't exist => return error. if it exists, check if password
    # from db matches password received from client. if they don't match => return error. else return success
    if existing_password is None:
        error = {
            "error": "--Failed to sign in. Invalid username or password."
        }
        return error, 401

    if password != existing_password:
        error = {
            "error": "--Failed to sign in. Invalid username or password."
        }
        return error, 401

    return '', 200


if __name__ == "__main__":
    app.run(port=3008, debug=True)