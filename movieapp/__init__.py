from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SECRET_KEY']='f6854380a4d38593662c150272a571d4'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/movieapp'
db=SQLAlchemy(app)

from movieapp import routes