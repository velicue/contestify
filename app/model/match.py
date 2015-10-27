from app import db

class Match(db.EmbeddedDocument):
	player1Id = db.ObjectIdField()
	player2Id = db.ObjectIdField()
	score1 = db.IntField()
	score2 = db.IntField()

class MatchList(db.Document):
	contestId = db.ObjectIdField()
	matches = db.ListField(db.EmbeddedDocumentField(Match))
