import asyncio
from play import play
from jsonStream import readJson, writeJson


# Se connecter au serveur du championnat et demande d'inscription
async def inscription(Host_Ip, Port_Ip, request):
    '''
    :param Host_Ip: adresse Ip du serveur du championnat
    :param Port_Ip: port distant
    :param request: message inscription a envoyer au serveur
    :return: réponse du serveur
    '''
    try:
        reader, writer = await asyncio.open_connection(Host_Ip, Port_Ip)
        print('connection au serveur établie')
        await writeJson(writer, request)
        response = await readJson(reader)
        writer.close()
    except:
        print('connection non établie')
        response = 'not OK'

    return response


# Lancer le serveur
async def start_server(PORT, alg):
    server = await asyncio.start_server(lambda r,w: dialogue(r, w, alg), '0.0.0.0', PORT)
    print(f"Le serveur écoute sur le port {PORT}, avec l'algorithme {alg} ")
    async with server:
        await server.serve_forever()


# Dialogue avec le serveur du championnat
async def dialogue(reader, writer, alg):
    message = await readJson(reader)
    request = message['request']
    print(message)
    if request == 'ping':
        await writeJson(writer, {"response": "pong"})
    elif request == 'play':
        msg = play(message, alg)
        await writeJson(writer, msg)
    writer.close()
    await writer.wait_closed()