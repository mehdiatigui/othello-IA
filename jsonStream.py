import json
import asyncio


async def ReadJson(reader: asyncio.StreamReader):
    data = ''
    chunk = await reader.read(512)
    message = chunk.decode('utf8')
    data = json.loads(message)
    return data


async def WriteJson(writer: asyncio.StreamWriter, obj):
    message = json.dumps(obj).encode()
    writer.write(message)
    await writer.drain()
