from flask import Flask, request
from flask_cors import CORS

from study_buddy_app.repository_g608 import connect_to_database, DB_FILE, get_user_profile, update_user_profile

app = Flask("MyProfileApi")
CORS(app)


@app.route("/api/v1/my-profile/<user_id>", methods=["GET", "PUT"])
def my_profile(user_id):
    if request.method == "GET":
        try:
            conn = connect_to_database(DB_FILE)
            profile = get_user_profile(conn, user_id)
            conn.close()

            if not profile:
                error = {
                    "error": f"--Failed to get user profile. Cause: User id {user_id} doesn't exist."
                }
                return error, 404
            return profile, 200
        except Exception as e:
            error = {
                "error": f"--Failed to get user profile. Cause: {e}"
            }
            return error, 500

    if request.method == "PUT":
        try:
            body = request.json
            conn = connect_to_database(DB_FILE)
            update_user_profile(conn, body, user_id)
            conn.close()

            return '', 204
        except Exception as e:
            error = {
                "error": f"--Failed to update user {user_id}. Cause: {e}"
            }
            return error, 500


if __name__ == "__main__":
    app.run(port=3018, debug=True)
