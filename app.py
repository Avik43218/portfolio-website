from fastapi import Request
from source import create_app, templates
from fastapi.responses import HTMLResponse

app = create_app()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    context = {
        "request": request,
        "header": "Welcome",
        "message": "Welcome to our site!"
    }

    return templates.TemplateResponse(request, "home.html", context)
    # return {"message": "Welcome to our site!"}
