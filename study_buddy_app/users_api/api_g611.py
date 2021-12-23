from flask import Flask, request
from flask_cors import CORS

from study_buddy_app.repository_g611 import database, connect_to_database, create_user, get_email_and_password


app = Flask("UsersAPI")
CORS(app)


@app.route("/api/v1/sign-up", methods=["POST"])
def signup():
    try:
        body = request.json
        conn = connect_to_database(database)
        create_user(conn, body)
        conn.close()
        return '', 204
    except Exception as e:
        error = {
            "error": f"--Failed to create user. Cause: {e}"
        }
        return error, 500


@app.route("/api/v1/sign-in", methods=["POST"])
def sign_in():
    try:
        body = request.json
        email = body.get("email")
        password = body.get("password")

        conn = connect_to_database(database)
        user = get_email_and_password(conn, email)
        if not user:
            error = {
                "error": "--Failed to sign in. User or password are wrong."
            }
            return error, 401

        if password != user[1]:
            error = {
                "error": "--Failed to sign in. User or password are wrong."
            }
            return error, 401

        return '', 204
    except Exception as e:
        error = {
            "error": f"--Failed to sign in. Cause: {e}"
        }
        return error, 500


if __name__ == "__main__":
    app.run(debug=True, port=3011)