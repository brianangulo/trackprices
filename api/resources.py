from flask_restful import Resource

class HelloFromPy(Resource):
    def get(self):
        return {"hello": "world"}