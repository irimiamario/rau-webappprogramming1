# todo: cannot import module seminar8. check why this is the case
from flask import Flask
from flask_restful import Resource, Api

from seminar8.todo import ToDoList 

app = Flask(__name__)
api = Api(app)


class Calendar(Resource):
    pass


api.add_resource(ToDoList, '/to-do', '/to-do/<string:id>')
api.add_resource(Calendar, '/calendar')

if __name__ == "__main__":
    app.run(debug=True)
