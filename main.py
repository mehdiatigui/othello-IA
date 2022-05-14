import asyncio
import sys
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
    # Host_Ip = '172.17.33.118'
    Host_Ip = 'localhost'
    Port_Ip = 3000
    request = {
        "request": "subscribe",
        "port": info.port,
        "name": info.name,
        "matricules": [f"{info.matricule}"]
    }
    print(sys.argv)
    message = await inscription(Host_Ip, Port_Ip, request)

    try :
        if message['response'] == 'ok':
            await start_server(info.port, info.alg)
    except:
        time.sleep(3)
        print('reconnection....')
        await othello(info)


mehdi = MyInfo('mehdi', int(sys.argv[1]), '20081', 'minimax')
#ali = MyInfo('ali', int(sys.argv[2]), '20059', 'random')

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        othello(mehdi),
        # othello(ali),
    )
)
