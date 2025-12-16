from fastapi import FastAPI, Request
import os
import requests
import json

app = FastAPI()

CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

@app.get("/")
def root():
    return {"message": "FastAPI on Cloud Run is running"}

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()

    # メッセージイベントだけ処理
    events = body.get("events", [])
    for event in events:
        if event.get("type") == "message":
            reply_token = event["replyToken"]
            user_message = event["message"]["text"]

            reply(reply_token, user_message)

    return "OK"


def reply(reply_token: str, text: str):
    url = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    data = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text": f"受け取ったよ：{text}"
            }
        ]
    }
    requests.post(url, headers=headers, data=json.dumps(data))
