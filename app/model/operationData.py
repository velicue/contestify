#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: operationData.py
# $Date: 2015-12-06 17:20
# $Author: Matt Zhang <mattzhang9[at]gmail[dot]com>
from app import db
from util import *
from datetime import date, timedelta
class OperationData(db.Document):
    date = db.DateTimeField()
    contest = db.IntField()
    views = db.IntField()

    meta = {
        'indexes':[
            'date', 'views'
        ],
        'ordering':['-date']
    }

    @classmethod
    def increaseContests():
       date = date.today()
       today_doc = OperationData.get_one({'date':{'$gte':date-timedelta(day=1)}})
       if today_doc is None:
           op = OperationData(date=date, contest=0, views=0)
       else:
           op['contest'] = op['contest'] + 1
       op.save()
