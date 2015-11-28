#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: util.py
# $Date: 2015-11-27 23:02
# $Author: Matt Zhang <mattzhang9[at]gmail[dot]com>

from config import *


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
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

if __name__ == '__main__':
    send_email("mattzhang9@gmail.com", "Test", "testing")
