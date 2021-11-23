from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<h1>Helloooo from Flaaask</h1>"

@app.route("/data")
def data():
    user_info = {
        'username': 'luch',
        'name': 'andrei',
        'country': 'ro'
    }
    return user_info

if __name__ == "__main__":
    app.run(debug=True)