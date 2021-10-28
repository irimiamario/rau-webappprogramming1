from flask import Response
from flask_restful import Resource, request
import json


todos = []


class ToDoList(Resource):
    def get(self, id=None):
        if id is not None:
            resource = None
            for todo in todos:
                if todo["id"] == id:
                    resource = todo
                    break
            todos_json = json.dumps(resource)
        else:
            todos_json = json.dumps(todos)
        response = Response(response=todos_json, status=200,
                            content_type="application/json")
        return response

    def post(self):
        body = request.json
        todos.append(body)
        response = Response(status=200, content_type="application/json")
        return response

    def put(self, id):
        # for index, todo in enumerate(todos):
        #     if todo["id"] == id:
        #         break
        for index in range(0, len(todos)):
            if todos[index]["id"] == id:
                break
        if index < len(todos):
            todos[index] = request.json
            response = Response(status=200, content_type="application/json")
        else:
            response = Response(
                response='{"error": "Resource is missing"}', status=404, content_type="application/json")
        return response

    def delete(self, id):
        resource = None
        for todo in todos:
            if todo["id"] == id:
                resource = todo
                break
        if resource is not None:
            todos.remove(resource)
            response = Response(status=200, content_type="application/json")
        else:
            response = Response(
                response='{"error": "Resource is missing"}', status=404, content_type="application/json")
        return response
