from flask_restful import Resource, reqparse, request
import json
from app import db

parser = reqparse.RequestParser()
parser.add_argument("name")

class ShoppingList(Resource):
    def get(self):
        return  [
            {
                "name": "bread",
                "id": "1"
            },
            {
                "name": "milk",
                "id": "2"
            },
            {
                "name": "coffee",
                "id": "3"
            },
            {
                "name": "water",
                "id": "4"
            },
            {
                "name": "rice",
                "id": "5"
            }
        ]
    def post(self):
        data =json.loads(request.get_data())
        print(data)
        return data


       