from model.contest import Contest
from model.playerlist import PlayerList
from model.match import Match, MatchList
from model.graph import Graph1
from model.graph import Graph1Item

import usermanage

def get_contest_list():
	return Contest.objects()

def get_contest_by_id(contest_id):
	return Contest.objects(id = contest_id)[0]

def new_contest(contest_info):
	ncontest = Contest(title = contest_info['title'], format = contest_info['format'], totalPlayers = contest_info['totalPlayers'], description = contest_info['description'], game = contest_info['game'], currentPlayers = 0, progress = "")
	ncontest.save()
	new_player_list(ncontest.id, contest_info['totalPlayers'])
	generate_match_list(ncontest.id)
	generate_graph(ncontest.id)
	return ncontest

def get_player_list_by_contest_id(contest_id):
	return PlayerList.objects(contestId = contest_id)[0]

def new_player_list(contest_id, player_num):
	nplayer_list = PlayerList(contestId = contest_id, userIds = [])
	for i in range(int(player_num)):
		nplayer_list.userIds.append(usermanage.get_user_by_name("Player", str(i)).id)
	nplayer_list.save()

def register_player(contest_id, user_id):
	contest = Contest.objects(id = contest_id)[0]
	player_list = PlayerList.objects(contestId = contest_id)[0]
	user_id_to_substitute = player_list.userIds[contest.currentPlayers]
	player_list.userIds[contest.currentPlayers] = user_id
	player_list.save()
	contest.currentPlayers += 1
	contest.save()
	for i in Match.objects(player1Id = user_id_to_substitute):
		i.player1Id = user_id
		i.save()
	for i in Match.objects(player2Id = user_id_to_substitute):
		i.player2Id = user_id
		i.save()

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

def get_graph_by_contest_id(contest_id):
	return Graph.objects(contestId = contest_id)[0]

def generate_graph(contest_id):
	contest = get_contest_by_id(contest_id)
	player_list = get_player_list_by_contest_id(contest_id)
	if contest.format == "Single Round-Robin":
		n = contest.totalPlayers
		items = []
		for i in range(0, n):
			item = Graph1Item(playerId = player_list.userIds[i], win = 0, lose = 0, draw = 0, winPoints = 0, losePoints = 0, totalPoints = 0)
			items.append(item)
		graph = Graph1(contestId = contest_id, items = items)
		graph.save()

def upload_match_result(match_id, contest_id, score1, score2):
	contest = get_contest_by_id(contest_id)
	match = get_match_by_id(match_id)
	match.score1 = score1
	match.score2 = score2
	graph = get_graph_by_contest_id()
	if score1 > score2:
		p1 = 3
		p2 = 0
		w1 = 1
		w2 = 0
		l1 = 0
		l2 = 1
		d1 = 0
		d2 = 0
	elif score1 < score2:
		t1 = 0
		t2 = 3
		w1 = 0
		w2 = 1
		l1 = 1
		l2 = 0
		d1 = 0
		d2 = 0
	else:
		t1 = 1
		t2 = 1
		w1 = 0
		w2 = 0
		l1 = 0
		l2 = 0
		d1 = 1
		d2 = 1
	if contest.format == "Single Round-Robin":
		n = contest.totalPlayers
		for i in range(0, n):
			if graph.items[i].playerId == match.player1Id:
				graph.items[i].win += w1
				graph.items[i].lose += l1
				graph.items[i].draw += d1
				graph.items[i].winPoints += score1
				graph.items[i].losePoints += score2
				graph.items[i].totalPoints += p1
			if graph.items[i].playerId == match.player2Id:
				graph.items[i].win += w2
				graph.items[i].lose += l2
				graph.items[i].draw += d2
				graph.items[i].winPoints += score2
				graph.items[i].losePoints += score1
				graph.items[i].totalPoints += p2
		graph.save()
