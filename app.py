from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

load_dotenv()
REF_URL = os.getenv('REF_URL')
CUSTOM_DOMAIN = os.getenv('CUSTOM_DOMAIN')

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def redirect_to_custom_domain(request: Request, call_next):
    host = request.headers.get("host", "")
    if host.endswith("onrender.com"):
        url = str(request.url).replace(host, CUSTOM_DOMAIN)
        return RedirectResponse(url=url)
    return await call_next(request)


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


@app.api_route("/health", methods=["GET", "HEAD", "POST", "PUT"])
async def health_check():
    return {"status": "ok"}


@app.get("/how-to-make-quotex-account-in-pakistan", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("ar1.html", {"request": request})