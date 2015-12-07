#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: response.py
# $Author: Matt Zhang <mattzhang9[at]gmail[dot]com>
from flask import jsonify

def response(status, msg, result):
	return jsonify({'status': status, 'msg': msg, 'result': result})
