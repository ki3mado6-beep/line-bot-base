from fastapi import FastAPI, Request
import requests
import json

app = FastAPI()

CHANNEL_ACCESS_TOKEN = "hIHiDM3hQpF1Lhi5LlnAQTGCSdRxKs1UrZms7MwQJIVajiwrvFA+rPz6tzqTVPaPO5ENB29WlRs01sl31nw8b2Xpl0omz4Yyx3GrQnZg+LxbSyr2j3UDoGH8q4rwoavJFNmODH7ieCJxNlaebcT3WAdB04t89/1O/w1cDnyilFU="
USER_ID = "Udd1943e221b989db073025ee129241cb"

@app.post("/webhook")
async def webhook(request: Request):
    push_message("強制pushテスト")
    return "OK"


def push_message(text: str):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    data = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    requests.post(url, headers=headers, data=json.dumps(data))
