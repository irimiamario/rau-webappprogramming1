# pip install flask
from flask import Flask
from flask import request

app = Flask(__name__)

todos = []


@app.route("/")
def hello_world():
    return '<h1 style="color: red">Hello World</h1>'


@app.route("/say-hello")
def hello():
    personal_details = {
        "name": "Andrei",
        "age": 32,
        "location": "Romania"
    }
    return personal_details


@app.route("/todo", methods=['GET', 'POST', 'DELETE'])
def todo():
    if request.method == "GET":
        response = {
            "todos": todos
        }
        return response

    if request.method == "POST":
        data = request.json
        todos.append(data)
        return '', 200

    if request.method == "DELETE":
        data = request.json
        if "id" not in list(data.keys()):
            return "", 400

        resource = None
        for r in todos:
            if r["id"] == data["id"]:
                resource = r
                break
        if resource is not None:
            todos.remove(resource)
            return '', 200
        else:
            return '', 404


if __name__ == "__main__":
    app.run(host="localhost", port=3003, debug=True)

