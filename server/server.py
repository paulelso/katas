# server.py
from flask import Flask

SECRET_MESSAGE = "stay hard"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE
