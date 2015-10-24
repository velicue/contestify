from model.user import User
from mongoengine.errors import NotUniqueError

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
		return True
	else:
		return False