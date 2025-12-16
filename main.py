from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI on Cloud Run is running"}

from fastapi import Request

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.body()
    print(body)
    return "OK"
