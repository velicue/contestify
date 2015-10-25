from app import db
from flask.ext.login import UserMixin

class User(db.Document, UserMixin):
	email = db.StringField(required = True, unique = True)
	pwd = db.StringField(required = True)