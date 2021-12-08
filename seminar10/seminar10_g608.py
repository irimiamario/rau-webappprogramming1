from flask import Flask, request

from seminar8.sqlite_repository import connect, edit_user

app = Flask(__name__)

DB_FILE = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/user_management_api/db/users.db"


@app.route("/users/<user_id>", methods=["PUT"])
def update_or_delete_user(user_id):
    if user_id is None:
        response = {
            "error": "--Invalid user id. Please provide a valid user id."
        }
        return response, 400

    details = request.json
    if not details:
        response = {
            "error": "--Invalid data provided. Please provide a valid payload."
        }
        return response, 400

    try:
        conn = connect(DB_FILE)
        edit_user(conn, user_id=user_id, details=details)
        conn.close()
        response = ""
        status = 200
    except Exception as e:
        response = {
            "error": f"--Failed to update user. Error: {e}."
        }
        status = 500
    return response, status


if __name__ == "__main__":
    app.run(port=3008, debug=True)