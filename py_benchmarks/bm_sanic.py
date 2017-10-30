from sanic import Sanic
from sanic.response import json, text
import sys
import logging
import asyncio
# from sanic.config import LOGGING

# my_logger
LOGGER = logging.getLogger('my_logger')

# # my_handler
# HANDLER = 'logging.StreamHandler'

# # my Formatter
# FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


# # Register your formatter
# LOGGING["formatters"]['my_formatter'] = {
#     'format' : FORMATTER,
#     'datefmt': '%Y-%m-%d %H:%M:%S',
# }
# # Register your Handler
# LOGGING['handlers']['my_handler'] = {
#     'class': HANDLER,
#     'formatter': 'my_formatter',
#     'stream': sys.stderr
# }
# # Register your LOGGER
# LOGGING["loggers"]['my_logger'] = {
#     'level': 'INFO',
#     'handlers': ['my_handler'],
# }


# LOGGING["loggers"].pop("network", None)
# LOGGING["handlers"].pop("accessStream", None)
# LOGGING["handlers"].pop("errorStream", None)

app = Sanic(__name__)
app.config.KEEP_ALIVE = False

@app.route("/test/<:string>", strict_slashes=True)
async def test(request, test):
    # LOGGER.info("Hello, World!")
    sessionid = request.cookies.get('sessionid')
    # await asyncio.sleep(1.0)
    # print()
    return text('OK')


@app.route("/", strict_slashes=True)
async def test(request):
    return json({})


def main():
    app.run(debug=True, access_log=True)


if __name__ == '__main__':
    main()
