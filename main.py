from flask import Flask, request, make_response
from slackclient import SlackClient
import os
import json
import requests

# Your app's Slack bot user token
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_VERIFICATION_TOKEN = os.environ.get("SLACK_VERTIFICATION_TOKEN")

# Slack client for Web API requests
slack_client = SlackClient(SLACK_BOT_TOKEN)

# Define Payload
button_message_payload = [
    {
        'attachment_type': "default",
        'callback_id': 'anomaly_label',
        'fallback': 'Interactive message for creating anomaly label',
        "actions": [
            {
                "name": "anomaly",
                "text": "異常",
                "type": "button",
                "value": "anomaly"
            },
            {
                "name": "normal",
                "text": "正常",
                "type": "button",
                "value": "normal"
            }
        ]
    }
]

app = Flask(__name__)

@app.route("/post", methods=["GET"])
def post_button_message():
    slack_client.api_call(
        "chat.postMessage",
        channel = "#anomaly_label",
        text = '以下のボタンを押してラベル付けしてね',
        attachments = button_message_payload
    )
    return make_response("", 200)

@app.route("/slack", methods=['POST'])
def slack_reply():

    # Parse the request payload
    form_json = json.loads(request.form["payload"])
    value = form_json["actions"][0]["value"]
    ts = form_json["message_ts"]

    if value == "anomaly" :
        text = "`異常`ラベルが記録されました"
    elif value == "normal" :
        text = "`正常`ラベルが記録されました"
    else :
        text = "`unknown`が記録されました"

    slack_client.api_call(
        "chat.postMessage",
        channel = "#anomaly_label",
        text = text,
        thread_ts = ts,
        reply_broadcast = False
    )

    return make_response("", 200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
