from flask_restful import Resource

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
        return {"hello": "hello"}




       