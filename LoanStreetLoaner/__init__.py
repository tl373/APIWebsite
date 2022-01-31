import os, json
from flask import request, render_template, redirect, url_for, flash, Flask, jsonify, Blueprint, make_response
from flask_bootstrap import Bootstrap
from flask_restful import Api, Resource
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from bs4 import BeautifulSoup
from wtforms import StringField, SubmitField, FormField, FloatField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

