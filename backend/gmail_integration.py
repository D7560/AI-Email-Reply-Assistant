"""
Optional Gmail integration helper.


Steps to enable:
1. Go to Google Cloud Console -> Create a project -> Enable Gmail API.
2. Create OAuth 2.0 Client ID (Desktop app) and download `credentials.json`.
3. Place `credentials.json` next to this file. The first run will open a browser to authorize
and create `token.json` containing user credentials.


Only enable if you want to auto-read and send emails.
"""


import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle


SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def gmail_service():
 creds = None
 if os.path.exists('token.json'):
  with open('token.json', 'rb') as f:
   creds = pickle.load(f)
 if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
   creds.refresh(Request())
  else:
   flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
   creds = flow.run_local_server(port=0)
  with open('token.json', 'wb') as f:
   pickle.dump(creds, f)
 service = build('gmail', 'v1', credentials=creds)
 return service



def list_unread(service, max_results=10):
 res = service.users().messages().list(userId='me', labelIds=['INBOX', 'UNREAD'], maxResults=max_results).execute()
 messages = res.get('messages', [])
 out = []
 for m in messages:
  msg = service.users().messages().get(userId='me', id=m['id'], format='full').execute()
  out.append(msg)
 return out




def send_email(service, to, subject, body_text):
 message = MIMEText(body_text)
 message['to'] = to
 message['subject'] = subject
 raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
 msg = {'raw': raw}
 sent = service.users().messages().send(userId='me', body=msg).execute()
 return sent