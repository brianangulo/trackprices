from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ShoppingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Item_Name %r>' % self.name