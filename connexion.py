from jsonStream import ReadJson, WriteJson
import asyncio
from play import play


# Pour se connecter au serveur du championnat
async def inscription(data):
    '''
    :param data: dictionnaire avec une demande d'inscription pour un individu
    :return: une réponse
    '''
    try:
        reader, writer = await asyncio.open_connection('127.0.0.1', 3000)
        # reader, writer = await asyncio.open_connection('10.12.12.3', 3000)
        print('connection établie')
        await WriteJson(writer, data)

        response = await ReadJson(reader)
        writer.close()

    except:
        print('connection non établie')
        response = 'not OK'
    return response

# lance le serveur
async def start_server(port):
    server = await asyncio.start_server(dialogue, 'localhost', port)

    async with server:
        await server.serve_forever()

# dialogue avec l'autre serveur
async def dialogue(reader, writer):
    msgReceived = await ReadJson(reader)
    message = ''

    # reçois ping et répond pong
    if msgReceived['request'] == 'ping':
        message = {"response": "pong"}
    # reçois play et répond le coup à jouer
    elif msgReceived['request'] == 'play':
        message = play(msgReceived)

    await WriteJson(writer, message)
    writer.close()
