from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info("Зашли в app.py")

app = Flask(__name__)




@app.route('/echo', methods=['POST'])
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

if __name__ == '__main__':
    logging.info("Зашли в app.run")
    app.run(threaded=True)
    