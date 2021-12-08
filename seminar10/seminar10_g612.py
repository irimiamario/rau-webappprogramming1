from flask import Flask, request

from seminar8.sqlite_repository import connect, delete_user

app = Flask(__name__)

DB_FILE = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/user_management_api/db/users.db"


def _erase_user(user_id):
    if not user_id or user_id == "null" or user_id == "undefined":
        response = {
            "error": f"--Failed to delete user. Invalid user id provided; user_id = {user_id}"
        }
        return response, 400

    try:
        conn = connect(DB_FILE)
        delete_user(conn, user_id=user_id)
        conn.close()
        return "", 200
    except Exception as e:
        response = {
            "error": f"--Failed to delete user. Error {e}"
        }
        return response, 500


@app.route('/api/v1/users/<user_id>', methods=["PUT", "DELETE"])
def erase_user(user_id):
    if request.method == "DELETE":
        _erase_user(user_id)

    if request.method == "PUT":
        response = {
            "message": "I don't know what you want me to do."
        }
        return response, 200


if __name__ == "__main__":
    app.run(port=3012, debug=True)