from model.user import User
from mongoengine.errors import NotUniqueError
from flask.ext.login import *
from flask.ext.login import login_user
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id = user_id)[0]

def register(userinfo):
	nuser = User(email = userinfo['email'], pwd = userinfo['pwd'])
	try:
		nuser.save()
		return True
	except NotUniqueError:
		return False

def login(userinfo):
	result = User.objects(email = userinfo['email'], pwd = userinfo['pwd'])
	
	if len(result) > 0:
		login_user(result[0])
		return True
	else:
		return False