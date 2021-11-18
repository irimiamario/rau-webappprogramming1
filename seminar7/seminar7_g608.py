# pip install flask
# pip install flask-restful
# pip install pysqlite3
from datetime import datetime

from seminar7.resources.hello import HelloWord


class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say_your_name(self):
        return self.__name

    def say_your_age(self):
        return self.__age

    def __age_up(self):
        if self.__age > 10:
            return None
        else:
            self.__age = self.__age + 1

    def change_name(self, name):
        if type(name) != str:
            raise Exception("Name must be a string.")
        self.__name = name

    def year_passed(self):
        self.__age_up()


def sample_animal_use_case():
    a = Animal('ruf', 10)
    print(f"Name = {a.say_your_name()}")
    print(f"Age = {a.say_your_age()}")

    a.change_name("Ruff")
    print(f"New name = {a.say_your_name()}")

    a.year_passed()
    print(f"New age = {a.say_your_age()}")

    # a.change_name(134)


from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def hello_world():
#     return {"name": __name__, "version": "1"}
#
#
# @app.route('/new-resource')
# def new_resource():
#     a = Animal("Ruff", 5)
#     a.year_passed()
#     response = {
#         'name': a.say_your_name(),
#         'age': a.say_your_age(),
#         'requested_at': datetime.now()
#     }
#     return response

api.add_resource(HelloWord, '/', '/home', '/index')

if __name__ == "__main__":
    app.run(debug=True, port=8000)



