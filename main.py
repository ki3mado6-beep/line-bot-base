from fastapi import FastAPI
import requests

app = FastAPI()

CHANNEL_ACCESS_TOKEN = "hIHiDM3hQpF1Lhi5LlnAQTGCSdRxKs1UrZms7MwQJIVajiwrvFA+rPz6tzqTVPaPO5ENB29WlRs01sl31nw8b2Xpl0omz4Yyx3GrQnZg+LxbSyr2j3UDoGH8q4rwoavJFNmODH7ieCJxNlaebcT3WAdB04t89/1O/w1cDnyilFU="

@app.get("/")
def root():
    return {"message": "alive"}

@app.get("/test-line")
def test_line():
    url = "https://api.line.me/v2/bot/profile/me"
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    return {
        "status_code": r.status_code,
        "text": r.text
    }
