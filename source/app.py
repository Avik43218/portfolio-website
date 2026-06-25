from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from users import routes

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(routes.users, prefix="",tags=["Users"])

@app.get("/")
def home():
    return {"message": "Welcome to our website!"}
