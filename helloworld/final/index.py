import sys

print 'Content-Type: text/html'
print ' '

#a form for awesomeness
print '''<form method="post" action="/">
What is your name?: <input type="text" name="fname"><br><br>
<input type="submit" value="Send data">
</form><hr>'''

#reading form input
form = sys.stdin.read()

try:
    fname = form[form.find('=')+1:]
except:
    fname = "?"

print '<p> Welcome, <span style="color: red">' + fname + ' </span>' + 'to <b>GDG.</b></p>' 
