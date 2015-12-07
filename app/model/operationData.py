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
    def increaseContests(self):
       today = date.today()
       today_doc = OperationData.objects(date__gte=today-timedelta(days=1))
       if len(today_doc) == 0:
           doc = OperationData(date=today, contest=0, views=0)
       else:
           doc = today_doc[0]
       doc.contest += 1
       doc.save()
    
    @classmethod
    def getContests(self,days):
       today = date.today()
       data = OperationData.objects(date__gte=today-timedelta(days=days))
       if data is None:
           return 0
       else:
           count = 0
           for i in data:
               count += i.contest
           return count

