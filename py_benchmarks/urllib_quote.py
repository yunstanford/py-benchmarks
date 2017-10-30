from urllib.parse import quote
import asyncio


async def quote_url(url):
	return quote(quote(url))


def main():
	import time
	coros = []
	loop = asyncio.get_event_loop()
	before = time.time()
	for i in range(1000):
		coros.append(quote_url("blabla~:::bla~~bla~~"))
	after = time.time()
	loop.run_until_complete(asyncio.gather(*coros))
	print(after - before)

if __name__ == '__main__':
	main()
