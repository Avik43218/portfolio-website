from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="source/templates")

def create_app():
    app = FastAPI()

    from .users.routes import users

    app.mount("/static", StaticFiles(directory="source/static"), name="static")
    app.include_router(users, prefix="",tags=["Users"])

    return app
