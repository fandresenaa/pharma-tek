from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

'''
Db configuration

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/pharma-tek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)


class Medocs:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)


class MedocsSchema:
    class Meta:
        fields = ('id', 'name', 'price')
# Route voloany


@app.route('/')
def home():
    return ('gg , ao amle API tsika ')


if __name__ == '__main__':
    app.run(debug=True)
