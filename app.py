# main.py
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

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
    redirect_url = "https://broker-qx.pro/sign-up/?lid=1608650"
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)


@app.get('/go/quotex/{slug}')
async def add(slug: str):
    redirect_url = "https://broker-qx.pro/sign-up/?lid=1608650"
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    redirect_url = "https://broker-qx.pro/sign-up/?lid=1608650"
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
