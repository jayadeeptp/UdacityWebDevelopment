import webapp2

form = """
<form method = "post" action = "/testform"> 
    <input name ="q"> 
    <input type = "submit">
</form>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
##        self.response.headers['Content-Type'] = 'text/plain'
##        self.response.write('Hello, Udacity!')
        self.response.write(form)

class TestForm(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.write(q)
##        self.response.headers['Content-Type'] = 'text/plain'
##        self.response.write(self.request)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestForm),

], debug=True)
