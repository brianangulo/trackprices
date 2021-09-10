from flask import Flask, app
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from resources import ShoppingList
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
CORS(app)
parser = reqparse.RequestParser()

api.add_resource(ShoppingList, '/hello')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
