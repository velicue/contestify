from app import db

class Contest(db.Document):
	title = db.StringField()
	format = db.StringField()
	totalPlayers = db.IntField()
	currentPlayers = db.IntField()
	description = db.StringField()
	progress = db.StringField()
	game = db.StringField()
	adminId = db.ObjectIdField()
	