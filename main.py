from application import create_app
import uvicorn
from fastapi import Request, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = create_app()


templates = Jinja2Templates(directory= 'templates')
app.mount('/static', StaticFiles(directory='static'), name = 'static')

@app.get('/')
def test(request : Request):
    return RedirectResponse(url='/dept/department-page', status_code = status.HTTP_302_FOUND)