from flask import Flask

app = Flask("myapp")


@app.route("/sample-mock", methods=["GET", "POST"])
def mock():
    # # aici e codul cu bug-uri
    # if request.method == "GET":
    #     response = {
    #         "todos": todos
    #     }
    #     return response
    #
    # if request.method == "POST":
    #     data = request.json
    #     todos.append(data)
    #     return '', 200
    #
    # if request.method == "DELETE":
    #     data = request.json
    #     if "id" not in list(data.keys()):
    #         return "", 400
    #
    #     resource = None
    #     for r in todos:
    #         if r["id"] == data["id"]:
    #             resource = r
    #             break
    #     if resource is not None:
    #         todos.remove(resource)
    #         return '', 200
    #     else:
    #         return '', 404

    # mock response, inca am bugs
    resp = {
        "data": [1, 2, 3, 4]
    }
    return resp, 200


if __name__ == "__main__":
    app.run(debug=True, port=3007)