# If you don't have flask & flask-restful installed, please
# open your command prompt or terminal, run the following commands:
#
# pip install flask
# pip install flask-restful
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get(self):
        data = {
            "name": self.__name,
            "age": self.__age
        }
        return data

    def put_name(self, name):
        self.__name = name

    def put_age(self, age):
        self.__age = age

    def put(self, name, age):
        self.__name = name
        self.__age = age

    def delete(self):
        self.__name = None
        self.__age = None


def sample():
    a = Animal("Ruf", 10)
    print(f"Name = {a.get_name()}")
    print(f"Age = {a.get_age()}")
    print(f"Name + age = {a.get()}")

    a.put("ruffff", 5)
    print(f"New name + age = {a.get()}")


from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"


@app.route("/animal-info")
def animal_info():
    a = Animal("Ruf", 10)
    response = a.get()
    return response


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=3002)

