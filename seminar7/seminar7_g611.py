# client <-> server <-> database
# === REQUEST ===
# headers
# url
# https://myapp.com/ = home
# https://myapp.com/api/v1/users
# verb: GET, POST, PUT, DELETE
# body: datele / detaliile a ceea ce vreau sa fac.
"""
    {
        "name": "andrei",
        "email": "a@a.com",
        "password": "fsdfkdslkjfds",
        ...
    }
"""
# === RESPONSE ===
# headers
# body
# status (200, 204, 400, 404, 401, 403, 503)

# user --> client app --> request --> webserver --> redirect to specific resource
# --> business logic to process request --> response --> webserver --> client app --> user

# please install flask for this to work
# pip install flask
from flask import Flask

app = Flask(__name__)


@app.route("/api/v1/hello-world", methods=["GET"])
def hello_world():
    return '<h1 style="color: red; font-size: 100px">Hello World</h1>'


@app.route("/")
def home():
    return '<h1 style="color: blue; font-size: 100px">Welcome to our API!</h1>'


@app.route("/sample-data")
def sample_data():
    response = {
        "data": [
            {
                "name": "a",
                "points": 100
            },
            {
                "name": "b",
                "points": 100
            },
            {
                "name": "c",
                "points": 100
            }
        ]
    }
    return response


if __name__ == "__main__":
    app.run(host="localhost", port=3011, debug=True)


