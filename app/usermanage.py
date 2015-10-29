from model.user import User

def get_user_list():
	return User.objects()

def get_user_by_id(user_id):
	return User.objects(id = user_id)[0]

def get_user_by_name(first_name, last_name):
	return User.objects(firstName = first_name, lastName = last_name)[0]