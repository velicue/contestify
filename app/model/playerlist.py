from app import db

class PlayerList(db.Document):
	contestId = db.ObjectIdField()
	userIds = db.ListField(db.ObjectIdField())