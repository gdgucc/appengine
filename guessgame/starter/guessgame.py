import webapp2

formstring = '''\
    <hr>
    <form method = "post" action= "/">
    <p>How old is my father: <input name="guess" type="number"></p>
    <input type="submit">
    </form>
    '''

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(formstring)

    def post(self):
        stguess = self.request.get('guess')

        try:
            guess = int(stguess)
        except:
            guess = -1

        answer = 25
        if guess == answer:
            msg = 'Congratulations'
            style = 'style="color: green"'
        elif guess > answer:
            msg = 'Your guess is too high'
            style = 'style="color: blue"'
        else:
            msg = 'Your guess is too low'
            style = 'style="color: red"'

        self.response.out.write('<p>Guess: ' + stguess + '</p>\n')
        self.response.out.write('<p ' + style + '>' + msg + '</p>\n')
        self.response.out.write(formstring)

application = webapp2.WSGIApplication(
        [('/', MainPage)],
        debug = True
        )
