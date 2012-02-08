# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Guest(db.Model):
  name = db.StringProperty()
  vegetarian = db.BooleanProperty()
  date = db.DateTimeProperty(auto_now_add=True)
