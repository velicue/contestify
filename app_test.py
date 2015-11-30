import os
from app import app
import unittest
import tempfile
import json

class appTestCase(unittest.TestCase):

	def setUp(self):
		app.config['MONGODB_SETTINGS'] = {
			'db': 'heroku_4n7dw5c8',
			'host': 'ds045464.mongolab.com',
			'port': 45464,
			'username': 'velicue',
			'password': 'KsMs13Mc'
		}

		self.app = app.test_client()

	def tearDown(self):
		return

	def test_root(self):
		rv = self.app.get('/')
		assert rv.status == '200 OK'

	def login(self, username, password):
		data = dict(
			email = username,
			password = password
		)
		return self.app.post('/login', data = json.dumps(data), content_type='application/json')

	def logout(self):
		return self.app.post('/logout')

	def current_user(self):
		return self.app.get('/currentUser')

	def test_login_logout(self):
		self.login('abc@abc.com', 'abcde')
		rv = self.current_user()
		resp = json.loads(rv.data)
		assert resp['result']['currentUserId'] != None
		self.logout()
		rv = self.current_user()
		resp = json.loads(rv.data)
		assert resp['result']['currentUserId'] == None

	def test_contest(self):
		rv = self.app.get('/publicContestList')
		data = json.loads(rv.data)
		assert len(data['result']) != 0
		cid = data['result'][0]['_id']['$oid']
		rv = self.app.get('/contest?id=' + cid)
		data = json.loads(rv.data)
		assert data['result']['title'] != None
		rv = self.app.get('/playerList?id=' + cid)
		data = json.loads(rv.data)
		assert len(data['result']['userIds']) != 0
		rv = self.app.get('/matchList?id=' + cid)
		data = json.loads(rv.data)
		assert len(data['result']['matches']) != 0
		mid = data['result']['matches'][0]['$oid']
		rv = self.app.get('/match?id=' + mid)
		data = json.loads(rv.data)
		assert data['result']['player1Id'] != None
		rv = self.app.get('/graph?id=' + cid)
		data = json.loads(rv.data)
		assert len(data['result']['items']) != 0
		
if __name__ == '__main__':
	unittest.main()