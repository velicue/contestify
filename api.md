# API

## JSON Response Format

```
{
	"status":
	"msg":
	"result": Described Below
}
```

## Id format

All objects have a `_id` property
```
{
	"$oid": String
}
```

## Login Page - Done

url: `/login`
method: `GET`

## Current User - Done

url: `/currentUser`
method: `GET`
response:

```
{
	"currentUserId": "562e883002074076e8c69bda"
}
```

## Login - Done

url: `/login`
method: `POST`
data: 

```
{
	"email": String,
	"password": String
}
```

## Logout - Todo

url: `/logout`
method: `POST`

## Signup - Done

url: `/register`
method: `POST`
data: 

```
{
	"firstName": String,
	"lastName": String
	"email": String,
	"password": String
}
```

## Get List of Contests - Done

url: `/publicContestList`
method: `GET`
response:

```
[{
	"id":
	"title": String,
	"format": String,
	"totalPlayers": Num,
	"currentPlayers": Num,
	"description": String,
	"progress": String,
	"game": String
}]
```

## Get the List of Players of a Contest - Done

url: `/playerList?id=contestid`
method: `GET`
response:

```
{
	"contestId":
	"userIds:": [
		ObjectID,
	]
}
```

## Get the Profile of a Player - Done

url: `/user?id=userid`
method: `GET`
response:

```
{
	"firstName": String,
	"lastName": String
	"email": String,
	"userType":
	"avatar": String,
}
```

## Get the Info of a Contest - Done

url: `/contest?id=contestid`
method: `GET`

## Get the Graph of a Contest - Todo

url: `/graph?id=contestid`
method: `GET`
response:

```
{
	"type": String,
	"contestId":
	"content": {
		"playerId":
		"win": Num,
		"lose": Num,
		"draw": Num,
		"winPoints": Num,
		"losePoints": Num,
		"totalPoints": Num
	} | [{
		"matchId":
		"childMatch1Id":
		"childMatch2Id":
	}]
}
```

## Get the Schedule of a Contest - Todo

url: `/matchList?id=contestid`
method: `GET`
response:

```
{
	"contestId":
	"matches": [
		ObjectId,
	]
}
```

## Get the Information of a Match - Todo

url: `/match?id=matchid`
method: `GET`
response:

```
{
	"player1Id":
	"player2Id":
	"score1": Num,
	"score2": Num,
	"day": Num
}
```

## Create a New Contest - Not Completed

url: `/contest`
method: `POST`
data:

```
{
	"title": String,
	"format": String,
	"totalPlayers": Num,
	"description": String,
	"game": String
}
```

response:

```
The same as contest
```

## Register for a Contest - Not Completed

url: `/playerList/<contest_id>`
method: `PUT`
data:

```
{
	"userId":
}
```

## Upload a Match Result - Todo

url: `/match/<match_id>`
method: `PUT`
data:

```
{
	"contestId":
	"score1": Num,
	"score2": Num
}
```
