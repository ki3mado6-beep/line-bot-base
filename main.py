from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI on Cloud Run is running"}

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()   # ← ここ重要
    print(json.dumps(body, ensure_ascii=False))
    return "OK"
