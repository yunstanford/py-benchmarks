

async def test_sanic_route(test_cli):
    resp = await test_cli.get('/')
    assert resp.status == 200
    assert (await resp.json()) == {"hello": "world"}


async def test_sanic_blueprint(test_cli):
    resp = await test_cli.get('/blueprint/bp')
    assert resp.status == 200
    assert (await resp.json()) == {"foo": "bar"}


async def test_pytest_init_db(test_cli):
    resp = await test_cli.get('/mongo')
    assert resp.status == 200
    assert (await resp.json()) == {
        "_id": "tag_123",
        "tag": [
            "mondev", "velocity"
        ]
    }
async def test_sanic_route_hi():
	pass