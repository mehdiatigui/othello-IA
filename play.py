from strategies import *


def play(msg, alg):
    '''
    :param msg: dictionnaire reçu du serveur
    :return: dictionnaire avec le move à jouer
    '''
    board = msg['state']['board']
    currentPlayer = msg['state']['current']

    # Liste des coups possible
    legalMoves = list(get_legal_moves(board, currentPlayer))
    move = None
    message = ''

    if alg == 'random':
        move, message = random_strategy(legalMoves)
    elif alg == 'minimax':
        move, message = minimax_strategy(board, legalMoves, currentPlayer)

    message = {
        "response": "move",
        "move": move,
        "message": message
    }
    return message