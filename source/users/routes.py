from fastapi import APIRouter

users = APIRouter()

@users.get("/route")
def route():
    return {"message": "This is a route!"}

@users.get("/login")
def login():
    pass
