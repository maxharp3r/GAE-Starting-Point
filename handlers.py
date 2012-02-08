# -*- coding: utf-8 -*-

import webapp2

from misc import BaseHandler
from models import Guest


class Root(BaseHandler):
    def get(self):
        self.render_response('docs.html')


class Simple(BaseHandler):
    def get(self, foo):
        context = {'a_variable': foo}
        self.render_response('simple.html', **context)


class SignUp(BaseHandler):
    def get(self):
        guests = Guest.all().order('-date').fetch(limit=100)
        context = {"post_action": webapp2.uri_for("signup"),
                   "guests": guests}
        self.render_response('signup.html', **context)

    def post(self):
        name = self.request.get('name')
        veg = (self.request.get("veg", default_value="false") == "true")

        new_guest = Guest(name=name, vegetarian=veg)
        new_guest.put()

        self.redirect_to("signup")
