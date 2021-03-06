from model.user import User
from mongoengine.errors import NotUniqueError
from flask.ext.login import *
#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: userauth.py
# $Date: 2015-11-08 9:19
# $Author: Matt Zhang <mattzhang9[at]gmail[dot]com>
from flask.ext.login import login_user
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.objects(id = user_id)[0]

def register(user_info, user_type):
	nuser = User(firstName = user_info['firstName'], lastName = user_info['lastName'], email = user_info['email'], password = user_info['password'], userType = user_type)
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
