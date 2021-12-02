from flask import Flask, request
from seminar8.sqlite_repository import connect, edit_user, delete_user

DB_FILE = "/Users/luchicila/work/rau-webappprogramming1/user_management_api/db/users.db"

app = Flask(__name__)


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass


@app.route("/users/<user_id>", methods=["PUT", "DELETE"])
def update_user(user_id):
    user_id = int(user_id)
    if request.method == "PUT":
        try:
            user_details = request.json
            conn = connect(DB_FILE)
            edit_user(conn=conn, user_id=user_id, details=user_details)
            conn.close()
            return "", 200
        except Exception as e:
            error = {
                "error": f"Failed to update user. Error message: {e}"
            }
            return error, 500
    if request.method == "DELETE":
        try:
            conn = connect(DB_FILE)
            delete_user(conn=conn, user_id=user_id)
            conn.close()
            return "", 200
        except Exception as e:
            error = {
                "error": f"Failed to delete user. Error message: {e}"
            }
            return error, 500


if __name__ == "__main__":
    app.run(debug=True, port=3005)