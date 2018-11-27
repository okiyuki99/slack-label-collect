from flask import Flask,request,make_response
import os
import json
import requests

app = Flask(__name__)

@app.route("/slack", methods=['POST'])
def post():
    URL = 'https://hooks.slack.com/services/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'
    payload = {
        "text": "POSTがきたよ",
        "username": "Anomaly Response"
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(URL, data=json.dumps(payload), headers=headers)
    return make_response("", 200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
