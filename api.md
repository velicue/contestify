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

```
{
	"$oid": String
}
```

## Login Page

url: `/login`
method: `GET`

## Login

url: `/login`
method: `POST`
data: 

```
{
	"email": String,
	"password": String
}
```

## Logout

url: `/logout`
method: `POST`

## Signup

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

## Get List of Contests

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

## Get the List of Players of a Contest

url: `/playerList?id=contestid`
method: `GET`
response:

```
{
	"contestId":
	[{
		"userId":
	}]
}
```

### Get the Profile of a Player

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

### Get the Info of a Contest

url: `/contest?id=contestid`
method: `GET`

### Get the Graph of a Contest

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

### Get the Schedule of a Contest

url: `/matchList?id=contestid`
method: `GET`
response:

```
[{
	"matchId":
	"contestId":
	"player1Id":
	"player2Id":
	"score1": Num,
	"score2": Num
}]
```

### Get the Information of a Match

url: `/match?id=matchid`
method: `GET`

### Create a New Contest

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

### Register for a Contest

url: `/contest/<contestid>`
method: `PUT`
data:

```
{
	"userid":
}
```

### Upload a Match Result

url: `/match/<matchid>`
method: `PUT`
data:

```
{
	"score1": Num,
	"score2": Num
}
```
