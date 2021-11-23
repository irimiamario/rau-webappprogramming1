from flask import Flask, request

from repository import create_connection, get_all_users, get_user_email_and_pass, insert_user


app = Flask(__name__)


@app.route("/api/v1/users", methods=["GET", "POST"])
def users():
    conn = create_connection("db/users.db")

    if request.method == "GET":
        users = get_all_users(conn)
        response = {
            'data': users
        }
        conn.close()
        return response, 200

    if request.method == "POST":
        user_data = request.json
        user_data = [
            user_data["username"],
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["password"]
        ]
        insert_user(conn, user_data)
        conn.close()
        return '', 200


if __name__ == "__main__":
    app.run(port=5006, debug=True)