from app import db
from flask.ext.login import UserMixin

class User(db.Document, UserMixin):
	email = db.StringField(required = True, unique = True)
	password = db.StringField(required = True)
	firstName = db.StringField()
	lastName = db.StringField()
	userType = db.IntField()
	avatar = db.StringField()