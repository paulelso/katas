import os
from slack import WebClient

client = WebClient(token=os.environ['SLACK_API_TOKEN'])
response = client.conversations_members(channel=os.environ['SLACK_CHANNEL_ID'])