#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: usermanage.py
# $Date: 2015-10-01 9:53
# $Author: Matt Zhang <mattzhang9[at]gmail[dot]com>
from model.user import User

def get_user_list():
	return User.objects()

def get_user_by_id(user_id):
	return User.objects(id = user_id)[0]

def get_user_by_name(first_name, last_name):
	return User.objects(firstName = first_name, lastName = last_name)[0]
