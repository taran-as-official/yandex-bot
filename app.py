from flask import Flask, json, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/echo")
def index():
    logging.info("Запрос от Алисы: " + request.json)
    print("Запрос от Алисы (print): " +request.json)

    response = {
        
        "session": request.json["session"],
        "response": {
            "end_session": False
        },
        "version": request.json["version"]
    }
    response["response"]["text"] = 'Привет'
    logging.info(request.json)
    return json.dumps(response)

