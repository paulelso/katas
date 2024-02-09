import os
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    return creds