from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import List
from database.connection import conn

from routes.users import user_router
from routes.events import event_router


import uvicorn


app = FastAPI()

# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
