from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


APPNAME = "Terminal"
APPDESCRIPTION="Blog Website"
APPVERSION="V1.0"


templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", context={"request":request})


app = FastAPI(title=APPNAME, description=APPDESCRIPTION, version=APPVERSION)
app.include_router(router)
app.mount("/static", StaticFiles(directory="/"), name="static")
