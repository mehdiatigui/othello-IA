from dataclasses import dataclass

from connexion import inscription, start_server
import asyncio


@dataclass
class MyInfo:
    name: str
    port: int
    matricule: str

async def othello(info):
    myInfo = {
        "request": "subscribe",
        "port": info.port,
        "name": info.name,
        "matricules": [f"{info.matricule}"]
    }
    message = await inscription(myInfo)
    if message['response'] == 'ok':
        await start_server(info.port)


mehdi = MyInfo('mehdi', 4000, '20081')
ali = MyInfo('ali', 5000, '20058')
hussein = MyInfo('hussein', 6000, '20088')
hassan = MyInfo('hassan', 7000, '20041')
karim = MyInfo('karim', 8000, '20084')
fatima = MyInfo('fatima', 9000, '20041')
hadj = MyInfo('hadj', 1000, '20082')
muima = MyInfo('muima', 2000, '20063')
zak = MyInfo('zak', 3500, '20076')
adil = MyInfo('adil', 3100, '20077')
abdou = MyInfo('abdou', 3200, '20078')
ilham = MyInfo('ilham', 3300, '20079')
nora = MyInfo('nora', 3400, '20080')




loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        othello(mehdi),
        othello(ali),
        # othello(hussein),
        # othello(hassan),
        # othello(karim),
        # othello(fatima),
        # othello(hadj),
        # othello(muima),
        # othello(zak),
        # othello(adil),
        # othello(abdou),
        # othello(ilham),
        # othello(nora),
    )
)
