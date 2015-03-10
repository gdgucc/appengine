import sys

print 'Content-Type: text/html'

print ' '

# this is a form
print '''<form method="post" action="/">
<p>What is your name: <input type="text" name="username"></p>
<input type="submit" value="Send data">
</form>
<hr>'''

#reading post data
data = sys.stdin.read()

try:
    username = data[data.find('=')+1:]
except:
    username = 'Default'

print '<p> Welcome to GDG', username
