from model.user import User

def get_user_list():
	return User.objects()

def get_user_by_id(user_id):
	return User.objects(id = user_id)[0]