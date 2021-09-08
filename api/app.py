from flask import Flask, app
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources import HelloFromPy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

api.add_resource(HelloFromPy, '/hello')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
