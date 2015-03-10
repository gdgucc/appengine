import webapp2
from google.appengine.ext.webapp import template
import os

class MainPage(webapp2.RequestHandler):
    def get(self):
        temp = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        outstr = template.render(temp, {'hint' : 'Good luck!'})
        self.response.write(outstr)

    def post(self):
        stguess = self.request.get('guess')
		
	try:
            guess = int(stguess)
        except:
            guess = -1

        answer = 56
        if guess == answer:
            msg = 'Congratulations'
            tyle = "color: green"
        elif guess > answer:
            msg = 'Your guess is too high'
            tyle = "color: blue"
        else:
            msg = 'Your guess is too low'
            tyle = "color: red"
		
	temp = os.path.join(os.path.dirname(__file__), 'templates/guess.html')
        outstr = template.render(temp, {'hint':msg, 'stguess':stguess, 'style':tyle})
	self.response.write(outstr)
		
		
application = webapp2.WSGIApplication(
        [('/', MainPage)],
        debug = True
    )

