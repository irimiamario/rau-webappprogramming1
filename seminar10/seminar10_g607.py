from flask import Flask, request

from seminar8.sqlite_repository import connect, edit_user, delete_user

app = Flask(__name__)

DB_FILE = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/user_management_api/db/users.db"


@app.route('/api/v1/users/<user_id>', methods=["PUT", "DELETE"])
def modify_user(user_id):
    if user_id is None:
        response = {
            "error": f"--Invalid user id provided, {user_id}. Please try again using a valid id."
        }
        return response, 400

    if request.method == "PUT":
        user_details = request.json
        if not user_details:
            response = {
                "error": f"--Invalid user details provided. user_details={user_details}."
            }
            return response, 400

        try:
            conn = connect(DB_FILE)
            edit_user(conn, user_id=user_id, details=user_details)
            conn.close()
            return "", 200
        except Exception as e:
            response = {
                "error": f"--Failed to update user details. Error: {e}."
            }
            return response, 500

    if request.method == "DELETE":
        try:
            conn = connect(DB_FILE)
            delete_user(conn, user_id=user_id)
            conn.close()
            return "", 200

        except Exception as e:
            response = {
                "error": f"--Failed to delete user. Error: {e}."
            }
            return response, 500


if __name__ == "__main__":
    app.run(port=3007, debug=True)