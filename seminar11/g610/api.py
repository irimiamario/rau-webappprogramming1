# create a flask application 

# create an endpoint that accepts a POST request and creates a user 

# extract data (user details) from request body 

# check if password and secondPassword are the same 

# if they don't match, create error and return error + status (400)

# if they match:
    # connect to a database 

    # create user = insert in database 

    # if no errors, return 204 

    # if error, create error message and return error + status 
from flask import Flask, request 
from flask_cors import CORS 

from repository import connect_to_database, create_user


app = Flask("UserManagementAPI")
CORS(app)

database_path = "/Users/luchicila/work/rau/teaching/rau-webappprogramming1/seminar11/database/basic_users.db"

@app.route("/api/v1/users", methods=["POST"])
def users():
    # extract data (user details) from request body 
    body = request.json

    # check if password and secondPassword are the same 
    # if they don't match, create error and return error + status (400)
    if body["password"] != body["secondPassword"]:
        error = {
            "error": "--Failed to create user. Passwords don't match."
        }
        return error, 400

    try:    
        # create a list with user details
        user_details = [
            body["firstName"],
            body["lastName"],
            body["email"],
            body["password"]
        ]

        # connect to a database
        conn = connect_to_database(database_path)
        
        # create a user in db
        create_user(conn, user_details)
        conn.close()

        return "", 204
    except Exception as e:
        # return an error if something goes wrong
        error = {
            "error": f"--Failed to create user. Message: {e}"
        }
        return error, 500


app.run(debug=True, port=3010)