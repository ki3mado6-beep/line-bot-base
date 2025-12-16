@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()

    events = body.get("events", [])
    for event in events:
        reply_token = event.get("replyToken")
        if reply_token:
            reply(reply_token, "生きてる")

    return "OK"
