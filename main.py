# -*- coding: utf-8 -*-

import webapp2
from webapp2 import Route

app = webapp2.WSGIApplication([
    Route(r'/', handler='handlers.Root', name="root"),
    Route(r'/simple/<foo>', handler='handlers.Simple', name="simple"),
    Route(r'/signup', handler='handlers.SignUp', name="signup"),
], debug=True)

if __name__ == '__main__':
    app.run()
