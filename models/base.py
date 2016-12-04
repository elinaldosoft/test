#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from pymongo.collection import Cursor
import settings
from lib import inflect
p = inflect.engine()

__author__ = '@elinaldosoft'

cli = MongoClient(settings.DATABASE.get('HOST', 'localhost'))
db = cli[settings.DATABASE.get('DB', 'testdb')]


class Base(object):
    collection = Cursor

    __abstract__ = True

    def __init__(self):
        self.collection = db[p.plural(self.__class__.__name__.lower())]

    def first(self):
        return self.collection.find_one()

    def find_by(self, query=dict):
        return self.collection.find_one(query)
