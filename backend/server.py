from flask import Flask, jsonify, request
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

'''
Db configuration

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/pharma-tek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


ma = Marshmallow(app)


class Medocs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(100))

    def __init__(self, name, price):
        self.name = name
        self.price = price


class MedocsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price')


medoc_schema = MedocsSchema()
medocs_schema = MedocsSchema(many=True)
# Route voloany


@app.route('/')
def home():
    return ('gg , ao amle API tsika ')


@app.route('/allmed', methods=['GET'])
def get_medocs():
    all_medocs = Medocs.query.all()
    results = medocs_schema.dump(all_medocs)
    return jsonify(results)


@app.route('/add',methods=['POST'])
def add_medocs():
    name = request.json['name']
    price = request.json['price']

    meds = Medocs(name, price)
    db.session.add(meds)
    db.session.commit()
    return medocs_schema.jsonify(meds)


if __name__ == '__main__':
    app.run(debug=True)
