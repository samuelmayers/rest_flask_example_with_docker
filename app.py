import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from db import db, ma
from model import Form , FormSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'docker'),
    os.getenv('DB_PASSWORD', ''),
    os.getenv('DB_HOST', 'mysql'),
    os.getenv('DB_NAME', 'docker')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)
Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    forms= Form.query.all()
    return render_template("index.html",forms=forms)

@app.route('/add', methods=['POST'])
def add():
    fullname=request.form['fullname']
    phone=request.form['phone']
    email=request.form['email']
    form=Form(fullname,phone,email)
    db.session.add(form)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<string:id>',methods=['POST','GET','PUT'])
def edit(id):
    form=Form.query.get(id)
    if request.method == "POST" or request.method == "PUT":
        form.fullname = request.form['fullname']
        form.email = request.form['email']
        form.phone = request.form['phone']
        db.session.commit()
        return redirect('/')
    return render_template("update.html", form=form)

@app.route('/delete/<id>', methods=['DELETE','GET'])
def delete(id):
    form=Form.query.get(id)
    db.session.delete(form)
    db.session.commit()
    return redirect('/')

@app.route('/api')
def apis():
    forms = Form.query.all()
    form_schema = FormSchema(many=True)
    op = form_schema.dump(forms)
    return jsonify({"Form":op})

@app.route('/api/<id>')
def api(id):
    form = Form.query.get(id)
    form_schema = FormSchema()
    op = form_schema.dump(form)
    return jsonify({"Form":op})

if __name__ == '__main__':
    app.run(port=4000)
