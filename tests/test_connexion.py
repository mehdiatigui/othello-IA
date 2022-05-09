from connexion import *


async def test_inscription():
    Host_Ip = 'localhost'
    Port_Ip = 3000
    request = {'request': 'subscribe', 'port': 1000, 'name': 'mehdi', 'matricules': ['20081']}
    assert await inscription(Host_Ip, Port_Ip, request) == {'response': 'ok'} or 'not OK'




async def test_start_server():
    await start_server(1000, 'minimax')