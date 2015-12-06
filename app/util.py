#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: util.py
# $Date: 2015-11-27 23:02
# $Author: Matt Zhang <mattzhang9[at]gmail[dot]com>

from config import *
from model.user import User


def send_email(recipient, subject, body):
    import smtplib

    gmail_user = EMAIL
    gmail_pwd = PWD
    FROM = EMAIL
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
    except:
        print "Failed to send email"

def send_digest():
    users = User.objects()
    body = """
        Long time no see! Come and see what's new contests on contestify!
    """
    count = 0
    for user in users:
        send_email(user.email, "Come and Read the latest Info!", body)
        count = count + 1
        if count > 0:
            break

    
