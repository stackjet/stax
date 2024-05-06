import uvicorn
import mangum

from typing import Union

from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/hello-world/")
async def hello_world():
    """Hello World API"""

    return {"message": "Hello World"}


# Check for Telegram Webhook Setup with NGROK: https://medium.com/@oktaykopcak/testing-your-telegram-bot-with-ngrok-a-step-by-step-guide-81c8c4a9a853
handler = Mangum(app)
