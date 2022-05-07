from strategies import *
import time


def play(msg, alg):
    '''
    :param msg: dictionnaire reçu du serveur
    :return: dictionnaire avec le move à jouer
    '''
    board = msg['state']['board']
    currentPlayer = msg['state']['current']
    players = msg['state']['players']
    player = players[currentPlayer]

    # Liste des coups possible
    legalMoves = list(get_legal_moves(board, currentPlayer))
    move = None
    message = ''

    if alg == 'random':
        move, message = random_strategy(legalMoves)
    elif alg == 'minimax':
        tic = time.perf_counter()
        if len(legalMoves) == 0:  # s'il ne reste aucune possibilité, jouer None
            move = None
        elif len(legalMoves) == 1:  # s'il ne reste qu'une seule possibilité, la jouer
            move = legalMoves[0]
        else:
            # Vérifier si un corner se trouve dans la liste
            try:
                best_move = getCorner(legalMoves)[0]
            # Sinon effectuer une recherche en profondeur avec l'algorithme minimax
            except:
                # nbr cases vides ?
                # empty = get_count_empty(board)
                DEPTH = 3
                best_val = -1000000
                best_move = None
                for move in legalMoves:
                    new_board = play_move(board, move, currentPlayer)
                    move_val = minimax(currentPlayer, new_board, DEPTH, False, -1000000, 1000000)
                    if move_val > best_val:
                        best_val = move_val
                        best_move = move
            move = best_move

        toc = time.perf_counter()
        message = 'move : ' + str(move) + f", time : {toc - tic:0.4f} seconds"
        print('------------------------------------------------------')
        print(player, ' plays ', move, f" in {toc - tic:0.4f} seconds")
        print('------------------------------------------------------')

    message = {
        "response": "move",
        "move": move,
        "message": message
    }

    return message