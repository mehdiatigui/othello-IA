from strategies import *


# retourner le message à envoyer au serveur du championnat avec le move à jouer
def play(msg, alg):
    '''
    :param msg: message reçu du serveur
    :param alg: l'algorithme à jouer
    :return: message à envoyer avec le move à jouer et le message à afficher
    '''

    board = msg['state']['board']
    currentPlayer = msg['state']['current']

    # Liste des coups possibles
    legalMoves = list(get_legal_moves(board, currentPlayer))
    move = None
    message = ''

    if alg == 'minimax':
        move, message = minimax_strategy(board, legalMoves, currentPlayer)
    elif alg == 'random':
        move, message = random_strategy(legalMoves)

    message = {
        "response": "move",
        "move": move,
        "message": message
    }
    return message
