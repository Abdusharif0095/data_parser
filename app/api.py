import os
from .aptoide import Aptoide
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory=os.getcwd())


@app.get('/get_url')
async def get(url: str) -> JSONResponse:
    aptoide = Aptoide()
    content, status = await aptoide.get(url)
    json_compatible_item_data = jsonable_encoder(content)
    return JSONResponse(content=json_compatible_item_data,
                        status_code=status)
