from app import db

class Graph1(db.Document):
	playerId = db.ObjectIdField()
	win = db.IntField()
	lose = db.IntField()
	draw = db.IntField()
	winPoints = db.IntField()
	losePoints = db.IntField()
	totalPoints = db.IntField()