from flask import Flask, request, jsonify,send_from_directory,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from dotenv import dotenv_values
import os


config = dotenv_values('.env')
username = config['USERNAME']
password = config['PASSWORD']
database_name = config['DATABASE_NAME']
database_host_name = config['DATABASE_HOST_NAME']
database_port = config['DATABASE_PORT']

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=f"postgresql://{username}:{password}@{database_host_name}:{database_port}/{database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='User'
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),primary_key=True)
    mobile_no=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(12),nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)