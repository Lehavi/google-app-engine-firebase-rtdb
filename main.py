import webapp2
import json

# The below 2 libs are not among the GAE Standard default 3rd party libs.
# In your laptop, install them with these steps:
# mkdir lib
# pip install -t lib/ oauth2client
# confirm that this step also installed httplib2 in \lib
# In your code dir, create a file called appengine_config.py with:
#	from google.appengine.ext import vendor
#	vendor.add('lib')

import httplib2
from oauth2client.client import GoogleCredentials

# Define firebase operations that will be allowed in the OAth key
_FIREBASE_SCOPES = [
    'https://www.googleapis.com/auth/firebase.database',
    'https://www.googleapis.com/auth/userinfo.email']
	
# Create an HTTP object with default server to server credentials
def _get_http():
    http = httplib2.Http()
    creds = GoogleCredentials.get_application_default().create_scoped(_FIREBASE_SCOPES)
    creds.authorize(http)
    return http

# Read Firebase RTDB	
def firebase_get(path):
    response, content = _get_http().request(path, method='GET')
    return json.loads(content)
	
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
	D = firebase_get('https://pitch-music-dev.firebaseio.com/yl-learn.json')
	self.response.write(json.dumps(D))	
		
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
