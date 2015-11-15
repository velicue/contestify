from app import db
class Graph1Item(db.EmbeddedDocument):
	playerId = db.ObjectIdField()
	win = db.IntField()
	lose = db.IntField()
	draw = db.IntField()
	winPoints = db.IntField()
	losePoints = db.IntField()
	totalPoints = db.IntField()
	
class Graph1(db.Document):
	contestId = db.ObjectIdField()
	items = db.ListField(db.EmbeddedDocumentField(Graph1Item))