from flask import Flask, request
from flask_cors import CORS


app = Flask("MyProfileAPI")
CORS(app)


@app.route("/api/v1/my-profile/<email>", methods=["GET", "PUT"])
def my_profile(email=None):
    if request.method == "GET":
        return f"Hello {email}", 200

    if request.method == "PUT":
        return f"Updating {email}", 200


if __name__ == "__main__":
    app.run(port=3012, debug=True)
