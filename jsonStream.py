import json
import asyncio


async def readJson(reader: asyncio.StreamReader):
    message = ''
    message_json = ''
    while True:
        chunk = await reader.read(100)
        message += chunk.decode('utf-8')
        try:
            message_json = json.loads(message)
            break
        except json.JSONDecodeError:
            pass
    return message_json


async def writeJson(writer: asyncio.StreamWriter, obj):
    message = json.dumps(obj).encode('utf-8')
    writer.write(message)
    await writer.drain()
