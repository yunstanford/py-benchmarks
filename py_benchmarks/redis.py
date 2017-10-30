import os, datetime, logging
from sanic import Sanic
from sanic import response
import asyncio
import uvloop
import aiohttp
import aioredis
from sanic.config import Config

redis_host = os.environ.get('redis_host', "localhost")
redis_port = int(os.environ.get('redis_port', 6379))

Config.REQUEST_TIMEOUT = 120

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = Sanic(__name__)

@app.listener('before_server_start')
async def before_server_start(app, loop):
	app.redis_pool = await aioredis.create_connection( (redis_host, redis_port), loop=loop )

@app.listener('after_server_stop')
async def after_server_stop(app, loop):
	app.redis_pool.close()
	await app.redis_pool.wait_closed()

@app.route('/fetch', methods=['GET'])
async def handle_request(request):
	print(request.body)
	data = await app.redis_pool.execute('lrange', 'text', 0, -1)
	return response.json({"data": data})

loop = asyncio.get_event_loop()

def main():
	app.run(host="0.0.0.0", port=8080, workers=4, debug=True)

if __name__ == '__main__':
	main()