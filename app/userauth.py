from model.user import User
from mongoengine.errors import NotUniqueError
from flask.ext.login import *
from flask.ext.login import login_user
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.objects(id = user_id)[0]

def register(user_info):
	nuser = User(firstName = user_info['firstName'], lastName = user_info['lastName'], email = user_info['email'], password = user_info['password'], userType = 0)
	try:
		nuser.save()
		return True
	except NotUniqueError:
		return False

def login(user_info):
	result = User.objects(email = user_info['email'], password = user_info['password'])
	if len(result) > 0:
		login_user(result[0])
		return True
	else:
		return False