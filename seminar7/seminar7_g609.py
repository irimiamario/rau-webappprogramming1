# client <-> server <-> database
# === REQUEST ===
# headers
# url
# https://myapp.com/users
# Method (VERB): GET, POST, PUT, DELETE
# Content (BODY):
"""
    {
        "name": "a",
        "email": "a@c.com",
        "password": "slkadjfk",
        ...
    }
"""
# === RESPONSE ===
# headers
# body
# status (200, 204, 400, 404, 401, 403, 503)
# client --> create-user-request -->
# Scenario 1: BE error --> 400 --> client --> retry with new body or prompt user to input data again
# Scenario 2: BE error --> 404 --> client --> redirect to other url
# Scenario 3: BE error --> 503 --> client --> snack bar informing the user to try again later...

# === REQUEST - RESPONSE CYCLE INTRO ====
# user --> client --> request --> webserver --> redirect to resource identified by URL -->
# run business logic to process request --> response --> webserver --> client --> user

# please install flask if  you want this to run
# pip install flask
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return '<h1 style="color: blue; font-size: 200px">Welcome to my first API!</h1>'


@app.route("/sample-data")
def sample_data():
    response = {
        "data": [
            {
                "name": 'a',
                "points": 100
            },
            {
                "name": 'b',
                "points": 2450
            }
        ]
    }
    return response


app.run(host="localhost", port=3009, debug=True)
