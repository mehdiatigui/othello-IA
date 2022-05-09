from jsonStream import *


async def test_readJson():
    reader, writer = await asyncio.open_connection('localhost', 3000)
    await readJson(reader)


async def test_writeJson():
    reader, writer = await asyncio.open_connection('localhost', 3000)
    msg = {
        "request": "subscribe",
        "port": 5000,
        "name": 'mehdi',
        "matricules": [24585]
    }
    await writeJson(writer, msg)