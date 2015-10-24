from app import db
from flask.ext.login import *

class User(db.Document):
	email = db.StringField(required = True, unique = True)
	pwd = db.StringField(required = True)