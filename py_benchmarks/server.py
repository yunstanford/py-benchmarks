from sanic import Sanic, Blueprint
from sanic.response import json
from pymongo.read_preferences import ReadPreference
import motor.motor_asyncio
import socket


app = Sanic()
bp = Blueprint("test_blueprints", url_prefix="/blueprint")

DB_NAME = "sanic-unit-tests-{hostname}".format(
    hostname=socket.gethostname())
DB_CONFIG = {
    "db_name": DB_NAME,
    "hosts": ",".join([
        "MONGOHOST",
        "MONGOHOST",
        "MONGOHOST"
    ]),
    "replicaset": "rs0",
    "max_pool_size": 10,
    "write_concern": 3
}


@app.route("/")
async def test(request):
    return json({"hello": "world"})

@bp.route("/bp")
async def test_blueprints(request):
    return json({"foo": "bar"})

app.blueprint(bp)

@app.route("/mongo")
async def test_mongo(request):
    doc = await request.app.mongo.tags.find_one()
    return json(doc)


@app.listener('before_server_start')
async def init_db(app, loop):
    print("===========**************")
    connection = motor.motor_asyncio.AsyncIOMotorClient(
        host=DB_CONFIG["hosts"],
        replicaset=DB_CONFIG["replicaset"],
        maxPoolSize=DB_CONFIG["max_pool_size"],
        read_preference=ReadPreference.PRIMARY_PREFERRED,
        w=DB_CONFIG["write_concern"]
    )
    db = connection[DB_CONFIG["db_name"]]
    app.mongo = db
    doc = {
        "_id": "tag_123",
        "tag": [
            "mondev", "velocity"
        ]
    }
    await app.mongo.tags.save(doc)


@app.listener('before_server_start')
def test_not_async_listener(app, loop):
    print("====== *********** =====")


@app.listener('after_server_stop')
async def close_db(app, loop):
    await app.mongo.command("dropDatabase")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
