# API

## Login

url: `/login`
method: `POST`
data: 

```
{
email: String,
password: String
}
```

return:

```
{
	status: String('success' or 'fail'),
	errorMessage: ''
}
```

## Logout

url: `/logout`
method: `POST`

return:

```
{
	status: String('success' or 'fail'),
	errorMessage: ''
}
```

## Signup

url: `/register`
method: `POST`
data: 

```
{
email: String,
password: String
}
```

return:

```
{
	status: String('success' or 'fail'),
	errorMessage: ''
}
```

