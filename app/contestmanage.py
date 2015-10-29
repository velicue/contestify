from model.contest import Contest
from model.playerlist import PlayerList
from model.match import Match, MatchList
from model.graph import Graph1

import usermanage

def get_contest_list():
	return Contest.objects()

def get_contest_by_id(contest_id):
	return Contest.objects(id = contest_id)[0]

def new_contest(contest_info):
	ncontest = Contest(title = contest_info['title'], format = contest_info['format'], totalPlayers = contest_info['totalPlayers'], description = contest_info['description'], game = contest_info['game'])
	ncontest.save()
	new_player_list(ncontest.id, contest_info['totalPlayers'])
	generate_match_list(ncontest.id)
	#generate_graph(ncontest.id)
	return ncontest

def get_player_list_by_contest_id(contest_id):
	return PlayerList.objects(contestId = contest_id)[0]

def new_player_list(contest_id, player_num):
	nplayer_list = PlayerList(contestId = contest_id, userIds = [])
	for i in range(int(player_num)):
		nplayer_list.userIds.append(usermanage.get_user_by_name("Player", str(i)).id)
	nplayer_list.save()

def insert_player_list(contest_id, user_id):
	player_list = PlayerList.objects(contestId = contest_id)[0]
	player_list.userIds.append(user_id)
	player_list.save()

def get_match_by_id(match_id):
	return Match.objects(id = match_id)[0]

def get_match_list_by_contest_id(contest_id):
	return MatchList.objects(contestId = contest_id)[0]
	
def generate_match_list(contest_id):
	contest = get_contest_by_id(contest_id)
	player_list = get_player_list_by_contest_id(contest_id)
	print player_list.userIds
	if contest.format == "Single Round-Robin":
		n = contest.totalPlayers
		if n % 2 == 0:
			matches = []
			for i in range(0, n - 1):
				for j in range(i, n - 1):
					t = (i + j) % (n - 1) + 1
					if i == j:
						player1_id = player_list.userIds[i]
						player2_id = player_list.userIds[n - 1]
					else:
						player1_id = player_list.userIds[i]
						player2_id = player_list.userIds[j]
					match = Match(player1Id = player1_id, player2Id = player2_id, score1 = -1, score2 = -1, day = t)
					match.save()
					matches.append(match)
		else:
			matches = []
			for i in range(0, n):
				for j in range(i, n):
					t = (i + j) % n + 1	
					if i == j:
						player1_id = player_list.userIds[i]
						player2_id = usermanage.get_user_by_name("", "BYE").id
					else:
						player1_id = player_list.userIds[i]
						player2_id = player_list.userIds[j]
					match = Match(player1Id = player1_id, player2Id = player2_id, score1 = -1, score2 = -1, day = t)
					match.save()
					matches.append(match)
		matches.sort(key = lambda Match: Match.day)
		match_list = MatchList(contestId = contest_id, matches = [])
		for i in matches: match_list.matches.append(i.id)
		match_list.save()