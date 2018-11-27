from flask import Flask, request, make_response
import os
import json
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return make_response("", 200)

@app.route("/slack", methods=['POST'])
def post():

    # Parse the request payload
    form_json = json.loads(request.form["payload"])
    value = form_json["actions"][0]["value"]
    ts = form_json["message_ts"]

    URL = 'https://hooks.slack.com/services/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'
 
    if value == "anomaly" :
        text = "異常ラベルが記録されました"
    elif value == "normal" :
        text = "正常ラベルが記録されました"
    else :
        text = "unknownが記録されました"

    payload = {
        "text": text,
        "username": "Anomaly Response",
        "thread_ts": ts,
        "reply_broadcast": False
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(URL, data=json.dumps(payload), headers=headers)
    return make_response("", 200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
