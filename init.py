from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'foos.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://foos:h7d3LrQ0@localhost:5432/foos'
db = SQLAlchemy(app)
ma = Marshmallow(app)
