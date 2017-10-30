from aiohttp import web
import aiohttp


async def handle(request):
    async with session.get('http://127.0.0.1:8000/') as resp:
        return web.json_response(await resp.json())


app = web.Application()
session = aiohttp.ClientSession()
app["session"] = session
app.router.add_get('/', handle)


def main():
    web.run_app(app, host='127.0.0.1', port=8080, access_log=None)


if __name__ == '__main__':
    main()
