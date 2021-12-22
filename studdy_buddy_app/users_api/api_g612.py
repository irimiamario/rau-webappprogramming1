from flask import Flask, request
from flask_cors import CORS

from studdy_buddy_app.repository_g612 import connect_to_database, database, create_user

app = Flask("UsersAPI")
CORS(app)


@app.route('/api/v1/sign-up', methods=["POST"])
def signup():
    try:
        body = request.json
        conn = connect_to_database(database)
        create_user(conn, body)
        conn.close()
        return '', 204
    except Exception as e:
        error = {
            "error": f"--Failed to create user. Message: {e}"
        }
        return error, 500


@app.route('/api/v1/sign-in', methods=["POST"])
def sign_in():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=3012)