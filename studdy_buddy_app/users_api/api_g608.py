from flask import Flask, request
from flask_cors import CORS

from studdy_buddy_app.repository_g608 import DB_FILE
from studdy_buddy_app.repository_g608 import connect_to_database, create_user

app = Flask("UsersAPI")
CORS(app)


@app.route("/api/v1/signup", methods=["POST"])
def signup():
    body = request.json
    try:
        conn = connect_to_database(DB_FILE)
        create_user(conn, body)
        conn.close()
    except Exception as e:
        error = {
            "error": f"--Failed to create user. Message {e}"
        }
        return error, 500


@app.route("/api/v1/sign-in", methods=["POST"])
def sign_in():
    pass


if __name__ == "__main__":
    app.run(port=3008, debug=True)