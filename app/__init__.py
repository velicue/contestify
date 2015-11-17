import httplib, urllib, json
import os
import flask, flask.views
from flask.ext.mongoengine import MongoEngine
from flask import jsonify
from flask.ext.login import *
from flask.ext.login import login_required
from flask.ext.login import current_user
from flask.ext.login import AnonymousUserMixin
from flask.ext.login import logout_user
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

@app.route('/')
def index():
	return app.send_static_file('index.html')

'''
@app.route("/",methods=["GET"])
@login_required
def protected():
	return flask.Response(response="Hello Protected World!" + current_user.email, status=200)
'''

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
	t = userauth.register(content, 0)
	if t:
		return response('OK', 'Registration Success.', None)
	else:
		return response('Failed', 'Registration Failed.', None)

@app.route('/registerEmptyUsers', methods=['POST'])
def register_empty_users_post():
	for i in range(int(128)):
		content = {}
		content["email"] = "Player" + str(i) + "@contestify.com"
		content["password"] = "QWERQWERQWER"
		content["firstName"] = "Player"
		content["lastName"] = str(i)
		t = userauth.register(content, 1)
	
	return response('OK', 'Batch Registration Success.', None)

@app.route('/registerTBDUser', methods=['POST'])
def register_TBD_user_post():
	content = {}
	content["email"] = "TBD" + "@contestify.com"
	content["password"] = "QWERQWERQWER"
	content["firstName"] = ""
	content["lastName"] = "TBD"
	t = userauth.register(content, 2)
	
	return response('OK', 'TBD Registration Success.', None)

@app.route('/registerBYEUser', methods=['POST'])
def register_BYE_user_post():
	content = {}
	content["email"] = "BYE" + "@contestify.com"
	content["password"] = "QWERQWERQWER"
	content["firstName"] = ""
	content["lastName"] = "BYE"
	t = userauth.register(content, 3)
	
	return response('OK', 'BYE Registration Success.', None)

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

@app.route('/match', methods=['GET'])
def match_get():
	contest_id = flask.request.args.get('id')
	t = contestmanage.get_match_by_id(match_id = contest_id)
	return response('OK', '', t)

@app.route('/matchList', methods=['GET'])
def match_list_get():
	contest_id = flask.request.args.get('id')
	t = contestmanage.get_match_list_by_contest_id(contest_id = contest_id)
	return response('OK', '', t)

@app.route('/graph', methods=['GET'])
def graph_get():
	contest_id = flask.request.args.get('id')
	t = contestmanage.get_graph_by_contest_id(contest_id = contest_id)
	return response('OK', '', t)

@app.route('/contest', methods=['POST'])
def contest_post():
	content = flask.request.json
	content['adminId'] = current_user.get_id()
	t = contestmanage.new_contest(content)
	return response('OK', 'New Contest Success.', t)

@app.route('/playerList/<contest_id>', methods=['PUT'])
def player_list_put(contest_id):
	content = flask.request.json
	contestmanage.register_player(contest_id = contest_id, user_id = content["userId"])
	return response('OK', '', None)

@app.route('/match/<match_id>', methods=['PUT'])
def upload_match_result(match_id):
	content = flask.request.json
	contestmanage.upload_match_result(match_id = match_id, contest_id = content["contestId"], score1 = content["score1"], score2 = content["score2"])
	return response('OK', '', None)


#static
@app.route('/<path:path>/')
def static_proxy_index(path):
	# send_static_file will guess the correct MIME type
	print path + 'index.html'
	return app.send_static_file(path)

@app.route('/<path:path>')
def static_proxy(path):
	# send_static_file will guess the correct MIME type
	print path
	return app.send_static_file(path)



