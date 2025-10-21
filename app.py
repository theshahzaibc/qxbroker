# main.py
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

load_dotenv()
REF_URL = os.getenv('REF_URL')

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# main.py (continued)
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about-quotex-pakistan", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/faqs", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("faqs.html", {"request": request})


@app.get("/blog", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})


@app.get("/article", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("article.html", {"request": request})


@app.get('/go/quotex')
async def add(request: Request):
    # add_student(name, surname, _class)  # Adding student data
    return RedirectResponse(REF_URL, status_code=status.HTTP_303_SEE_OTHER)


@app.get('/go/quotex/{slug}')
async def add(slug: str):
    return RedirectResponse(REF_URL, status_code=status.HTTP_303_SEE_OTHER)


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return RedirectResponse(REF_URL, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/health")
def health_check():
    return {"status": "ok"}
