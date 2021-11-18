# Background REST APIs
# client <-> server <-> database
# === REQUEST ===
# headers = meta information
# url = identifier
# ex: https://myapp.com/api/v1/users
# verb: GET (get resource(s)), POST (create resource(s)), PUT (update resource(s)), DELETE (delete resource(s)), OPTIONS
# (optional) body (json)
# GET https://myapp.com/api/v20/users?id=124356
# GET https://myapp.com/api/v20/users
# POST https://myapp.com/api/v1/users
"""
    {
        "name": "andrei",
        "email": "a@b.com",
        "password": "dlasjfdjiodjgfe"
    }
"""
# PUT https://myapp.com/api/v1/users?id=123465
"""
    {
        "name": "andrei"
    }
"""
# === RESPONSE ===
# headers
# (optional) body
# status (200, 204, 400, 404, 401, 403, 503)

# === REQUEST - RESPONSE CYCLE ===
# user --> client (FE) --> request (FE) --> webserver --> redirect to resource -->
# interpret request (BE) --> response (BE) --> webserver --> client (FE) --> user

# for this to work you need to install flask
# pip install flask
from flask import Flask


app = Flask("my app")


@app.route("/")
def home():
    return '<h1 style="color: blue; font-family: Courier">Welcome to my first API!</h1>'


@app.route("/sample-data")
def sample_data():
    resp = {
        "data": [
            {
                "name": "a",
                "id": 1,
                "points": 100
            },
            {
                "name": "b",
                "id": 2,
                "points": 1300
            },
            {
                "name": "c",
                "id": 12,
                "points": 100345
            }
        ]
    }
    return resp


app.run(host="localhost", port=3010, debug=True)
