import httplib, urllib, json
import os
import flask, flask.views
from flask.ext.mongoengine import MongoEngine
from flask import jsonify
from flask.ext.login import *

app = flask.Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'gamemasterdb',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

import userauth

class Main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')
	
app.add_url_rule('/',view_func=Main.as_view('main'), methods=["GET"])

@app.route('/api/user/register', methods=['POST'])
def register():
	content = flask.request.json
	t = userauth.register(content)
	print t
	if t:
		return flask.jsonify({'status': 'success'})
	else:
		return flask.jsonify({'status': 'fail'})

@app.route('/api/user/login', methods=['POST'])
def login():
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




	
