from os import name
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = True
api = Api(app)
db = SQLAlchemy(app)
CORS(app)
parser = reqparse.RequestParser()

#db models
class ShoppingItem(db.Model):
    """Shopping item db model"""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return self.name

def add_to_db(name) -> str:
        new_item = ShoppingItem(name=name)
        db.session.add(new_item)
        db.session.commit()

#Resources
class ShoppingList(Resource):
    """Shopping list resource"""

    def get(self):
        list_of_items = ShoppingItem.query.all()
        item_holder = [{  "name": item.name} for item in list_of_items]
        return item_holder

    def post(self):
        data =json.loads(request.get_data())
        add_to_db(data['name'])
        return '', 204


api.add_resource(ShoppingList, '/hello')

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)
