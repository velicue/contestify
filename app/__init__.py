import httplib, urllib, json
import os
import flask, flask.views
from flask.ext.mongoengine import MongoEngine
from flask import jsonify
from flask.ext.login import *
from flask.ext.login import login_required
from flask.ext.login import current_user

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

import userauth

@app.route("/",methods=["GET"])
@login_required
def protected():
    return flask.Response(response="Hello Protected World!" + current_user.email, status=200)

@app.route("/login",methods=["GET"])
def login_get():
	return flask.render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
	content = flask.request.json
	t = userauth.register(content)
	if t:
		return flask.jsonify({'status': 'success'})
	else:
		return flask.jsonify({'status': 'fail'})

@app.route('/login', methods=['POST'])
def login_post():
	content = flask.request.json
	t = userauth.login(content)
	print t
	if t:
		return flask.jsonify({'status': 'success'})
	else:
		return flask.jsonify({'status': 'fail'})

#static
@app.route('/<path:path>')
def static_proxy(path):
	# send_static_file will guess the correct MIME type
	print path
	return app.send_static_file(path)






	
