import httplib, urllib, json
import os
import flask, flask.views
from flask.ext.mongoengine import MongoEngine
from flask import jsonify
from flask.ext.login import *
from flask.ext.login import login_required
from flask.ext.login import current_user
from flask.ext.login import AnonymousUserMixin
from response import response

app = flask.Flask(__name__)

'''
app.config['MONGODB_SETTINGS'] = {
	'db': 'gamemasterdb',
	'host': 'localhost',
	'port': 27017
}
'''
app.config['MONGODB_SETTINGS'] = {
	'db': 'heroku_4n7dw5c8',
	'host': 'ds045464.mongolab.com',
	'port': 45464,
	'username': 'velicue',
	'password': 'KsMs13Mc'
}

db = MongoEngine()
db.init_app(app)

app.config["SECRET_KEY"] = "TOUMEININGEN"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_get"

@app.route("/",methods=["GET"])
@login_required
def protected():
	return flask.Response(response="Hello Protected World!" + current_user.email, status=200)

#authentication API
import userauth

@app.route("/login",methods=["GET"])
def login_get():
	return flask.render_template('login.html')

@app.route('/currentUser', methods=['GET'])
def current_user_get():
	t = {}
	t['currentUserId'] = current_user.get_id()
	return response('OK', '', t)

@app.route('/login', methods=['POST'])
def login_post():
	content = flask.request.json
	print content
	t = userauth.login(content)
	if t:
		return response('OK', 'Login Success.', None)
	else:
		return response('Failed', 'Login Failed.', None)

@app.route('/register', methods=['POST'])
def register_post():
	content = flask.request.json
	t = userauth.register(content)
	if t:
		return response('OK', 'Registration Success.', None)
	else:
		return response('Failed', 'Registration Failed.', None)

@app.route("/logout", methods=['POST'])
def logout():
	logout_user()
	return response('OK', 'Logout Success.', None)

#user API
import usermanage

@app.route("/userList", methods=["GET"])
def user_list_get():
	t = usermanage.get_user_list()
	return response('OK', '', t)

@app.route('/user', methods=['GET'])
def user_get():
	user_id = flask.request.args.get('id')
	t = usermanage.get_user_by_id(user_id = user_id)
	return response('OK', '', t)

#contest API
import contestmanage

@app.route('/publicContestList', methods=['GET'])
def public_contest_list_get():
	t = contestmanage.get_contest_list()
	return response('OK', '', t)

@app.route('/contest', methods=['GET'])
def contest_get():
	contest_id = flask.request.args.get('id')
	t = contestmanage.get_contest_by_id(contest_id = contest_id)
	return response('OK', '', t)

@app.route('/playerList', methods=['GET'])
def player_list_get():
	contest_id = flask.request.args.get('id')
	t = contestmanage.get_player_list_by_contest_id(contest_id = contest_id)
	return response('OK', '', t)

@app.route('/contest', methods=['POST'])
def contest_post():
	content = flask.request.json
	t = contestmanage.new_contest(content)
	return response('OK', 'New Contest Success.', t)

@app.route('/contest/<contest_id>', methods=['PUT'])
def contest_put(contest_id):
	content = flask.request.json
	contestmanage.insert_player_list(contest_id, content["userId"])
	return response('OK', 'Register Success.', None)

#static
@app.route('/<path:path>')
def static_proxy(path):
	# send_static_file will guess the correct MIME type
	print path
	return app.send_static_file(path)

