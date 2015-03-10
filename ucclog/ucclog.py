import os
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from util.sessions import Session


def doRender(handler, tname='index.html', values={}):
	temp = os.path.join(os.path.dirname(__file__), 'templates/' + tname)

	if not os.path.isfile(temp):
		return False

	# Make a copy of the dictionary and add the path
	newval = dict(values)
	newval['path'] = handler.request.path

	handler.session = Session()
	if 'username' in handler.session:
		newval['username'] = handler.session['username']

	outstr = template.render(temp, newval)
	handler.response.out.write(outstr)
	return True

#a model for a user
class User(db.Model):
	name = db.StringProperty()
	username = db.StringProperty()
	email = db.StringProperty()
	password = db.StringProperty()

class RegisterHandler(webapp2.RequestHandler):
	def get(self):
		doRender(self, 'account/register.html')

	def post(self):
		self.session = Session()
		fname = self.request.get('fname')
		uname = self.request.get('uname')
		acct = self.request.get('account')
		passwd = self.request.get('password')

		if fname == '' or uname == '' or acct == '' or passwd == '':
			doRender( self, 'account/register.html', {'error' : 'Please fill the form'})
			return

		# Check whether the user already exists
		que = db.Query(User)
		que = que.filter('email =',acct)
		results = que.fetch(limit=1)

		if len(results) > 0 :
			doRender(self,'account/register.html',{'error' : 'Account Already Exists'} )
			return

		# Create the User object and log the user in
		newuser = User(name=fname, username=uname, email=acct, password=passwd);
		newuser.put();
		self.session['username'] = acct
		doRender(self,'index.html',{'username' : self.session['username']})


class LoginHandler(webapp2.RequestHandler):
	def get(self):
		doRender(self, 'account/login.html')

	def post(self):
		self.session = Session()
		acct = self.request.get('account')
		passwd = self.request.get('password')

		if passwd == '' or acct == '':
			doRender( self, 'account/login.html', {'error' : 'Please specify email and password'})
                        return

                #Check the existence of the user
                que = db.Query(User);
                que = que.filter('email=', acct)
                que = que.filter('password=', passwd);
                results = que.fetch(limit=1)
                
		if len(results) > 0:
			self.session['username'] = acct
			doRender(self,'index.html',{'username' : self.session['username']})
		else:
			doRender(self, 'account/login.html',{'error' : 'Incorrect password'} )

class LogoutHandler(webapp2.RequestHandler):
	def get(self):
		self.session = Session()
		self.session.delete_item('username')
		doRender(self, 'index.html', {})

class MainHandler(webapp2.RequestHandler):
	def get(self):
		path = self.request.path
		if doRender(self, path):
			return

		doRender(self, 'index.html', {})


application = webapp2.WSGIApplication([
	('/login', LoginHandler),
	('/logout', LogoutHandler),
	('/register', RegisterHandler),
	('/.*', MainHandler)],
	debug=True)

