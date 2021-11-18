from flask_restful import Resource, request


database = []


class HelloWord(Resource):
    def get(self):
        response = {
            'data': database
        }
        return response

    def post(self):
        data = request.json
        database.append(data)
        return ''
