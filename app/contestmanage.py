from model.contest import Contest
from model.playerlist import PlayerList

def get_contest_list():
	return Contest.objects()

def get_contest_by_id(contest_id):
	return Contest.objects(id = contest_id)[0]

def new_contest(contest_info):
	ncontest = Contest(title = contest_info['title'], format = contest_info['format'], totalPlayers = contest_info['totalPlayers'], description = contest_info['description'], game = contest_info['game'])
	ncontest.save()
	new_player_list(ncontest.id)
	return ncontest

def get_player_list_by_contest_id(contest_id):
	return PlayerList.objects(contestId = contest_id)[0]

def new_player_list(contest_id):
	nplayer_list = PlayerList(contestId = contest_id, userIds = [])
	nplayer_list.save()

def insert_player_list(contest_id, user_id):
	player_list = PlayerList.objects(contestId = contest_id)[0]
	player_list.userIds.append(user_id)
	player_list.save()
	