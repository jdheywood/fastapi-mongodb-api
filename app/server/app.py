from fastapi import FastAPI

# from app.server.routes.student 

from .routes.student import router as StudentRouter

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello world"}


app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
