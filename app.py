from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/echo', methods=['POST'])
def index():

    response = {
        
        "session": request.json["session"],
        "response": {
            "end_session": False,
            "text": request.json["request"]["original_utterance"] 		
        },
        "version": request.json["version"]

    }

    return json.dumps(response)


