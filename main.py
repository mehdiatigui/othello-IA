import asyncio
from dataclasses import dataclass
from connexion import inscription, start_server


@dataclass
class MyInfo:
    name: str
    port: int
    matricule: str
    alg: str


async def othello(info):
    # se connecter au serveur de championnat
    Host_Ip = '10.12.12.63'
    # Host_Ip = 'localhost'
    Port_Ip = 3000
    request = {
        "request": "subscribe",
        "port": info.port,
        "name": info.name,
        "matricules": [f"{info.matricule}"]
    }

    message = await inscription(Host_Ip, Port_Ip, request)
    if message['response'] == 'ok':
        await start_server(info.port, info.alg)
    # else:
    #     await othello(info)


mehdi = MyInfo('mehdi', 5000, '20081', 'minimax')
# mehdi2 = MyInfo('mehdi2', 3001, '20082', 'minimax')
# mehdi3 = MyInfo('mehdi3', 3002, '20083', 'minimax')
ali = MyInfo('ali', 6000, '20058', 'random')
ali2 = MyInfo('ali2', 5002, '20052', 'random')
ali3 = MyInfo('ali3', 5003, '20053', 'random')
fatima = MyInfo('fatima', 7000, '20070', 'random')
fatima2 = MyInfo('fatima2', 7002, '20072', 'random')
fatima3 = MyInfo('fatima3', 7003, '20073', 'random')
hussein = MyInfo('hussein', 6001, '20088', 'random')
hussein2 = MyInfo('hussein2', 5500, '20012', 'random')
hussein3 = MyInfo('hussein3', 5600, '20013', 'random')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        othello(mehdi),
        # othello(mehdi2),
        # othello(mehdi3),
        # othello(ali),
        # othello(ali2),
        # othello(ali3),
        # othello(fatima),
        # othello(fatima2),
        # othello(fatima3),
        # othello(hussein),
        # othello(hussein2),
        # othello(hussein3),
    )
)
