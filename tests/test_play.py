from play import play


def test_play():
    message = {
        "response": "move",
        "move": 26,
        "message": 'message'
    }
    msg = {
        'request': 'play',
        'lives': 3,
        'errors': [],
        'state': {
            'players': ['ali', 'mehdi'],
            'current': 0,
            'board': [[28, 35], [27, 36]]}
    }

    play(msg, 'minimax')
    play(msg, 'random')
