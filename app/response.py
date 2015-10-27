from flask import jsonify

def response(status, msg, result):
	return jsonify({'status': status, 'msg': msg, 'result': result})