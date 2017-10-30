from .bm_sanic import app
from sanic.response import json


@app.route("/")
async def test(request):
    # LOGGER.info("Hello, World!")
    return json({"hello":"world"})