#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: service.py
# $Date: 2015-11-28 00:00
# $Author: Matt Zhang <mattzhang9[at]gmail[dot]com>

from util import send_digest


import time
import sched
import os
import threading
def perform():
    while True:
        send_digest()
        time.sleep(7200)

def emailService():
    t = threading.Thread(target=perform)
    t.setDaemon(True)
    t.start()  
