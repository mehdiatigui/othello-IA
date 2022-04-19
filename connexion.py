from jsonStream import ReadJson, WriteJson
import asyncio
from play import play


# Pour se connecter au serveur du championnat
async def inscription(data):
    try:
        reader, writer = await asyncio.open_connection('127.0.0.1', 3000)
        print('connection établie')
        await WriteJson(writer, data)

        response = await ReadJson(reader)
        writer.close()

    except:
        print('connection non établie')
        response = 'not OK'
    return response


async def start_server(port):
    server = await asyncio.start_server(dialogue, 'localhost', port)

    async with server:
        await server.serve_forever()


async def dialogue(reader, writer):
    msgReceived = await ReadJson(reader)
    # print(msgReceived)
    message = ''

    if msgReceived['request'] == 'ping':
        message = {"response": "pong"}
    elif msgReceived['request'] == 'play':
        message = play(msgReceived)

    await WriteJson(writer, message)
    writer.close()
