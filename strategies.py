import stopit
import random
import time

from utils import *


# Humain
# def humain(legalMoves):
#     print('legalmoves : ', legalMoves)
#     move = input('move choice:  ')
#     message = 'humain :' + move
#     try:
#         move = int(move)
#     except:
#         move = None
#
#     return move, message


# Random

def random_strategy(legalMoves_list):
    try:  # si liste n'est pas vide ==> random dans la site
        move = random.choice(legalMoves_list)
        message = "random :" + str(move)
        move = int(move)
    except:  # si liste vide ==> exception error
        print('Liste vide')
        move = None
        message = 'None'

    return move, message


# mehdi
Weights = [
    [100, -50, 10, 5, 5, 10, -50, 100],
    [-50, -75, 0, 0, 0, 0, -75, -50],
    [10, 0, 10, 0, 0, 10, 0, 10],
    [2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 2],
    [10, 0, 10, 0, 0, 10, 0, 10],
    [-50, -75, 0, 0, 0, 0, -75, -50],
    [100, -50, 10, 5, 5, 10, -50, 100]
]


# Weights2 = [
#     [500,   -100,   100,    50, 50, 100, -100, 500],
#     [-50,   -100,    -5,    -5, -5, -5, -100, -50],
#     [100,     -5,     5,    0, 0, 5, -5, 100],
#     [50,      -5,     0,       1, 1, 0, -5, 50],
#     [50,      -5,     0,       1, 1, 0, -5, 50],
#     [100,     -5,     5,    0, 0, 5, -5, 100],
#     [-50,    -75,    -5,    -5, -5, -5, -100, -50],
#     [500,   -100,   100,    50, 50, 100, -100, 500]
# ]


def get_Weight(index):
    row, col = get_coordinates(index)
    weight = Weights[row][col]
    return weight


def sorting_legal_moves_weighted(legalMoves_list):
    return sorted(legalMoves_list, key=get_Weight, reverse=True)


# Local Maximization
def weight_strategy(legalMoves_list):
    score = -9999
    move = None
    for cell in legalMoves_list:
        weight = get_Weight(cell)
        if weight > score:
            score = weight
            move = cell
    return move


# MiniMax
def play_move(board, move, current):
    '''
    :param board: Actual board
    :param move: next move
    :param current: which player
    :return: the new board
    '''
    playerColors = set(board[current])
    otherColors = board[abs(current - 1)]
    for direction in list_directions(move):
        cells_to_flip = set()
        for cell in direction:
            if cell in otherColors:
                cells_to_flip.add(cell)
            elif cell in playerColors:
                if len(cells_to_flip) > 0:
                    playerColors = playerColors.union(cells_to_flip)
                    otherColors = [x for x in otherColors if (x not in cells_to_flip)]
                break
            else:
                break

    playerColors.add(move)
    if current == 0:
        newboard = [list(playerColors), otherColors]
    else:
        newboard = [otherColors, list(playerColors)]
    return newboard


# update weight value
def update_weight_value(board, currentPlayer):
    myCorners, otherCorners = isCornerTaken(board, currentPlayer)
    new_weight = 150
    for corner in myCorners:
        if corner == 0 and get_Weight(1) != new_weight:
            change_weight_value([1, 8, 9], new_weight)
        if corner == 7 and get_Weight(6) != new_weight:
            change_weight_value([6, 14, 15], new_weight)
        if corner == 56 and get_Weight(48) != new_weight:
            change_weight_value([48, 49, 57], new_weight)
        if corner == 63 and get_Weight(54) != new_weight:
            change_weight_value([54, 55, 63], new_weight)
    new_weight = 0
    for corner in otherCorners:
        if corner == 0 and get_Weight(2) != new_weight:
            change_weight_value([2, 16], new_weight)
        if corner == 7 and get_Weight(5) != new_weight:
            change_weight_value([5, 23], new_weight)
        if corner == 56 and get_Weight(48) != new_weight:
            change_weight_value([48, 58], new_weight)
        if corner == 63 and get_Weight(61) != new_weight:
            change_weight_value([61, 47], new_weight)


# change weights
def change_weight_value(list_index, value):
    for cell in list_index:
        row, col = get_coordinates(cell)
        Weights[row][col] = value


def evaluation(board, current):
    evaluation = 0
    playerColors = board[current]
    otherColors = board[abs(current - 1)]

    for cell in playerColors:
        evaluation += get_Weight(cell)

    for cell in otherColors:
        evaluation -= get_Weight(cell)

    return evaluation


# Décorateur pour afficher move et temps execution
def move_time(f):
    def wrapper(*args):
        tic = time.time()
        result = f(*args)
        print(f'Played {result[0]}', 'in {:.3f} s'.format(time.time() - tic))
        print('-------------------')
        return result

    return wrapper


@move_time
def minimax_strategy(board, legalMoves, currentPlayer):
    tic = time.perf_counter()
    # vérifier si un coin est pris
    # si un coin est pris, changer le poid des cases adjacentes
    update_weight_value(board, currentPlayer)

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
            DEPTH = 4
            best_val = -1000000
            best_move = None

            with stopit.ThreadingTimeout(4.7) as context_manager:
                legalMoves = sorting_legal_moves_weighted(legalMoves) # trier selon le poid dans la plateau
                for move in legalMoves:
                    new_board = play_move(board, move, currentPlayer)
                    move_val = minimax(currentPlayer, new_board, DEPTH, False, -1000000, 1000000)
                    if move_val > best_val:
                        best_val = move_val
                        best_move = move

            # Si la recherche minimax n'a pas abouti en 9.5 secondes
            if context_manager.state == context_manager.TIMED_OUT:
                print("DID NOT FINISH...")
            # Sinon
            # elif context_manager.state == context_manager.EXECUTED:
            #     print("COMPLETE...")

        move = best_move

    message = 'Je joue ' + str(move) + f" en {time.perf_counter() - tic:0.2f} secondes"
    return move, message


def minimax(playerIndex, board, depth, maximizingPlayer, alpha, beta):
    otherPlayerIndex = (playerIndex + 1) % 2
    if depth == 0 or isGameOver(board):
        return evaluation(board, current=playerIndex)

    if maximizingPlayer:
        maxEval = -1000000
        legal_Moves = get_legal_moves(board, playerIndex)
        if len(legal_Moves) == 0:
            maxEval = minimax(playerIndex, board, depth, False, alpha, beta)
        else:
            for move in legal_Moves:
                # play move , get new board
                newBoard = play_move(board, move, playerIndex)
                eval = minimax(playerIndex, newBoard, depth - 1, False, alpha, beta)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval

    else:
        minEval = 100000
        legal_Moves = get_legal_moves(board, otherPlayerIndex)
        if len(legal_Moves) == 0:
            minEval = minimax(playerIndex, board, depth, True, alpha, beta)
        else:
            for move in legal_Moves:
                # play move , get new board
                newBoard = play_move(board, move, otherPlayerIndex)
                eval = minimax(playerIndex, newBoard, depth - 1, True, alpha, beta)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval
