Files here work in dev_appserver.py and also in GAE Standard.

There are 3 files
main.py
app.yaml
appengine_config.py

And a lib\ directory that containts
httplib2
oath2client

GAE must receive from you the 3 files and the lib\ in order to work.
gcloud app deploy will take care of it, and the appengine_config.py handle runtime.

Why it's not working:
Is the Firebase RTDB node referenced here still exists?
Did you define an environment variable called GOOGLE_APPLICATION_CREDENTIALS?
Did you obtain a key from Firebase (.json file) that this variable points to?