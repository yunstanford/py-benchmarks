from sanic import Sanic
from sanic.response import stream
import asyncio


app = Sanic(__name__)

@app.route("/")
async def test(request):
    async def sample_streaming_fn(response):
        response.write('foo\n')
        await asyncio.sleep(1)
        response.write('bar')
    return stream(sample_streaming_fn)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
