#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: util.py
# $Date: Sat Jul 04 14:42:03 2015 +0800
# $Author: He Zhang <mattzhang9[at]gmail[at]com>

from app import db
from functools import wraps

@classmethod
def _get_one(cls, *args, **kwargs):
    try:
        # print args, kwargs
        objs = cls.objects(*args, **kwargs)
        # print objs
        if len(objs) == 0:
            return None
        if len(objs) > 1:
            raise RuntimeError((
                "{}.get_one failed: more than one object with" +
                "  query:\n" +
                "    {}\n" +
                "    {}\n").format(cls.__name__, args, kwargs))
        return objs[0]
    except mongoengine.errors.ValidationError:
        return None
    except RuntimeError:
        return None


setattr(db.Document, 'get_one', _get_one)


def _save_update_timestamp(self, *args, **kwargs):
    if not self.creation_time:
        self.creation_time = datetime_now_local()
    self.modification_time = datetime_now_local()

    self.save(*args, **kwargs)

setattr(db.Document, 'save_update_timestamp', _save_update_timestamp)


@classmethod
def _increase(cls, id, name, delta=1, save=True):
    if isinstance(id, basestring):
        entity = cls.get_one(id=id)
    else:
        entity = id
    orig = getattr(entity, name)
    setattr(entity, name, orig + delta)
    if save:
        entity.save()
    return entity


def _instance_increase(self, name, delta=1):
    orig = getattr(self, name)
    setattr(self, name, orig + delta)
    return self


setattr(db.Document, 'increase', _increase)
setattr(db.Document, 'instance_increase', _instance_increase)