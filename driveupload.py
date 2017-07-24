#!/usr/bin/python

import httplib2
import pprint
import sys

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

v = sys.argv
CLIENT_ID = '686459762974-gtlc6bbu916es8ic7svhf137umvhc7qp.apps.googleusercontent.com'
CLIENT_SECRET = 'RFf0RdCJGkjApXebFOaegL5Y'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Path to the file to upload
FILENAME = str(v[1])

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, redirect_uri="urn:ietf:wg:oauth:2.0:oob")
authorize_url = flow.step1_get_authorize_url()
print ('Go to the following link in your browser: ' + authorize_url)
code = input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)
x=str(v[1]).split('.')
if(str(x[1])=='mp4'):
    y="video/mp4"
if(str(x[1])=='jpg'):
    y="image/jpg"
if(str(x[1])=='txt'):
    y="text/txt"


# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype=y, resumable=True)
body = {
 'title': str(v[1]),

}

file = drive_service.files().insert(body=body, media_body=media_body).execute()

