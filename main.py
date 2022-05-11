import asyncio
import time
from dataclasses import dataclass
from connexion import inscription, start_server


@dataclass
class MyInfo:
    name: str
    port: int
    matricule: str
    alg: str


async def othello(info):
    # se connecter au serveur du championnat
    # Host_Ip = '10.12.12.63'
    Host_Ip = 'localhost'
    Port_Ip = 3000
    request = {
        "request": "subscribe",
        "port": info.port,
        "name": info.name,
        "matricules": [f"{info.matricule}"]
    }

    message = await inscription(Host_Ip, Port_Ip, request)

    try :
        if message['response'] == 'ok':
            await start_server(info.port, info.alg)
    except:
        time.sleep(3)
        print('reconnection....')
        await othello(info)


mehdi = MyInfo('mehdi', 5000, '20081', 'minimax')
ali = MyInfo('ali', 6000, '20058', 'random')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        othello(mehdi),
        othello(ali),
    )
)