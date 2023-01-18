from revChatGPT.ChatGPT import Chatbot
from flask import Flask, request
import logging
from waitress import serve
from paste.translogger import TransLogger
import sys
import traceback

chatbot = Chatbot({
  "session_token": "<YOUR_TOKEN>"
}, conversation_id=None, parent_id=None) # You can start a custom conversation

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
  request_data = request.get_json()
  response = chatbot.ask(request_data['message'], conversation_id=None, parent_id=None)
  return response

if __name__ == "__main__":
    from waitress import serve
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.INFO)
    serve(TransLogger(app), host='0.0.0.0', port=8080)
