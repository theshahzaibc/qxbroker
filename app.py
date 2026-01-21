import json
import logging
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv
from data import articles
from datetime import date

load_dotenv()
REF_URL = os.getenv('REF_URL')
CUSTOM_DOMAIN = os.getenv('CUSTOM_DOMAIN')

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def redirect_to_custom_domain(request: Request, call_next):
    host = request.headers.get("host", "")
    if host.endswith("railway.app"):
        url = str(request.url).replace(host, CUSTOM_DOMAIN)
        return RedirectResponse(url=url, status_code=301)
    return await call_next(request)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/pk/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/quotex-market/", response_class=HTMLResponse)
async def market(request: Request):
    return templates.TemplateResponse("market.html", {"request": request})


@app.get("/quotex-trading/", response_class=HTMLResponse)
async def trading(request: Request):
    return templates.TemplateResponse("quotex-trading.html", {"request": request})


@app.get("/quotex-demo/", response_class=HTMLResponse)
async def demo_account(request: Request):
    return templates.TemplateResponse("quotex-demo.html", {"request": request})


@app.get("/quotex-login/", response_class=HTMLResponse)
async def demo_account(request: Request):
    return templates.TemplateResponse("quotex-login.html", {"request": request})


@app.get("/qxbroker-com/", response_class=HTMLResponse)
async def qxbrokercom(request: Request):
    return templates.TemplateResponse("qxbrokercom.html", {"request": request})


@app.get("/quotex/promo-code/", response_class=HTMLResponse)
async def promo_codes(request: Request):
    today = date.today()
    xmas_target_date = date(2025, 12, 27)
    supper_target_date = date(2025, 12, 27)
    is_xmas_ended = xmas_target_date <= today
    is_super_ended = supper_target_date <= today
    return templates.TemplateResponse("promo.html",
                                      {"request": request, "is_xmas_ended": is_xmas_ended,
                                       "is_super_ended": is_super_ended})


@app.get("/quotex/weekly-promo-code-bonus-today/", response_class=HTMLResponse)
async def weekly_promo_codes(request: Request):
    today = date.today()
    xmas_target_date = date(2025, 12, 27)
    supper_target_date = date(2025, 12, 27)
    is_xmas_ended = xmas_target_date <= today
    is_super_ended = supper_target_date <= today
    return templates.TemplateResponse("promo2.html",
                                      {"request": request, "is_xmas_ended": is_xmas_ended,
                                       "is_super_ended": is_super_ended})


@app.get("/about-quotex-pakistan/", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/faqs/", response_class=HTMLResponse)
async def faqs(request: Request):
    return templates.TemplateResponse("faqs.html", {"request": request})


@app.get("/blog/", response_class=HTMLResponse)
async def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})


@app.get("/article/", response_class=HTMLResponse)
async def base_article(request: Request):
    return templates.TemplateResponse("article.html", {"request": request})


@app.get('/go/quotex/')
async def goto(request: Request):
    # add_student(name, surname, _class)  # Adding student data
    response = RedirectResponse(REF_URL, status_code=302)
    response.headers["Referrer-Policy"] = "no-referrer"
    return response


@app.get('/go/quotex/{slug}/')
async def goto(slug: str):
    response = RedirectResponse(REF_URL, status_code=302)
    response.headers["Referrer-Policy"] = "no-referrer"
    return response


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    response = RedirectResponse(REF_URL, status_code=302)
    response.headers["Referrer-Policy"] = "no-referrer"
    return response


@app.api_route("/health", methods=["GET", "HEAD", "POST", "PUT"])
async def health_check():
    return {"status": "ok"}


@app.get("/sitemap.xml", response_class=HTMLResponse)
async def sitemap(request: Request):
    return templates.TemplateResponse("sitemap.xml", {"request": request, "articles": articles})


@app.get("/{ar_slug}/", response_class=HTMLResponse)
async def article(request: Request, ar_slug: str):
    page = [ar for ar in articles if ar['url'] == ar_slug]
    if not len(page):
        response = RedirectResponse(REF_URL, status_code=302)
        response.headers["Referrer-Policy"] = "no-referrer"
        return response
    return templates.TemplateResponse(page[0]['page'], {"request": request})
