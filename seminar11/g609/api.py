# import necessary libraries
from flask import Flask, request
from flask_cors import CORS

from seminar11.g609.repository import connect, create_user

# create a flask app
app = Flask("UserManagementAPI")

# add cors to the app
CORS(app)

DB_FILE = '/Users/luchicila/work/rau/teaching/rau-webappprogramming1/seminar11/database/basic_users.db'

# create the user endpoint (/api/v1/users) that accepts a POST method
# for this endpoint define a function users() with the following functionality
# 1. get request body
# 2. check if the request body is empty or not
# 2.1. if the request body is empty, return an error with a relevant message and status 400
# 3. create a try / except block containing the following functionality
# 3.1. try branch
# 3.1.1. Connect to the database using the connect() method in repository.py
# 3.1.2. Convert the request body into a list with the values in the same order as expected by the create_user() method
#       from repository.py
# 3.1.3. check if password and second_password are the same
# 3.1.3.1 if the passwords don't match, create an error with a relevant message and return with status code 400
# 3.1.4. create a user using the create_user() method in repository.py
# 3.1.5. return an empty response with status 204
# 3.2. except branch
# 3.2.1. create an error with a relevant message
# 3.2.2. return the error with status 500
@app.route("/api/v1/users", methods=["POST"])
def users():
    body = request.json
    if not body:
        error = {
            "error": "--Failed to create a new user. Empty body provided."
        }
        return error, 400

    try:
        first_password = body["password"]
        second_password = body["secondPassword"]
        if first_password != second_password:
            error = {
                "error": "--Failed to create user. Password mismatch."
            }
            return error, 400

        conn = connect(DB_FILE)
        user_details = [
            body["firstName"],
            body["lastName"],
            body["email"],
            body["password"]
        ]

        create_user(conn, user_details)
        conn.close()

        return '', 204
    except Exception as e:
        error = {
            "error": f"--Failed to create a new user. Message: {e}"
        }
        return error, 500


app.run(debug=True, port=3004)