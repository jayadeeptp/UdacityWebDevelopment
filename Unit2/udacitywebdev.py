import webapp2
import python_func

form = """
<form method = "post" > 
    What is you birthday
    <br>
    <label> Month
        <input type="text" name="month">
    </label>
    <label> Day
        <input type="text" name="day">
    </label>
    <label> Year
        <input type="text" name="year">
    </label>
    <br>
    <br>
    <input type = "submit">
</form>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(form)

    def post(self):
        user_month = python_func.valid_month(self.request.get('month'))
        user_day = python_func.valid_day(self.request.get('day'))
        user_year = python_func.valid_year(self.request.get('year'))

        if not(user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.write("Thanks! That's a totally valid day!")

application = webapp2.WSGIApplication([
    ('/', MainPage),

], debug=True)
