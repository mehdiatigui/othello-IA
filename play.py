import random
import numpy as np
# from minimax import minimax

# pour avoir les 8 directions possibles
directions = [
    (0,  1),
    (0, -1),
    (1,  0),
    (-1,  0),
    (1,  1),
    (-1,  1),
    (1, -1),
    (-1, -1)
]

### FAIRE SON TEST ###
# lance d'autres fonctions pour permettre de jouer un coup adéquat
# (sans bad moves et stratégique)
def play(msg):
    '''
    :param msg: dictionnaire reçu avec des clés et leurs valeurs
    :return: dictionnaire qui contient le coup à jouer
    '''
    board = msg['state']['board']
    current = msg['state']['current']
    try:
        legalMoves = legal_moves(board, current)
        if current == 1:
            move = random.choice(legalMoves)
        else:
            for m 
        print(move)
    except:
        move = None

    message = {
        "response": "move",
        "move": move,
        "message": str(move)
    }
    return message

# sert à donner les coordonnées
def get_coordinates(index):
    '''
    :param index: un numéro entre 0 et 63 sur la board
    :return: ligne et colonne
    '''
    row = index // 8
    col = index % 8
    return row, col

# regarde si les coordonnées sont à l'intérieur du plateau 8*8
def is_inside(row, col):
    '''
    :param row: ligne
    :param col: colonne
    :return: Vrai si dans board 8*8
    '''
    if 0 <= row < 8 and 0 <= col < 8:
        return True

# reçois des coordonnées et retourne l'index
def get_index(row, col):
    '''
    :param row: ligne
    :param col: colonne
    :return: index
    '''
    return row * 8 + col

### FAIRE SON TEST ###
# permet de trouver les différentes directions possibles pour l'index
def list_directions(index):
    '''
    :param index: nombre (compris entre 0 et 63)
    :return: les listes directionnelles
    '''
    for dir in directions:
        list = []
        row, col = get_coordinates(index)
        while is_inside(row, col):
            row += dir[0]
            col += dir[1]
            list.append(get_index(row, col))
        list.pop()
        yield list

# donne une liste de coups possibles
def legal_moves(board, current):
    '''
    :param board: une liste qui contient 2 listes (une pour les noirs sur le plateau, l'autre pour les blancs)
    :param current: reçois 0 pour noir et 1 pour blanc
    :return: liste de coups possibles
    '''
    legalMoves = []
    myColor = board[current]
    otherColor = board[abs(current-1)]
    for elem in myColor:
        for list in list_directions(elem):
            listOtherColor = []
            for cell in list:
                if cell in otherColor:
                    listOtherColor.append(cell)
                elif cell in myColor:
                    break
                else:
                    if len(listOtherColor) > 0:
                        legalMoves.append(cell)
                    break
    return legalMoves

Tactic_Mtx = [
    [100, -50, 10, 5, 5, 10, -50, 100],
    [-50, -75,  0, 0, 0,  0, -75, -50],
    [ 10,   0, 10, 0, 0, 10,   0,  10],
    [  2,   0,  0, 0, 0,  0,   0,   2],
    [  2,   0,  0, 0, 0,  0,   0,   2],
    [ 10,   0, 10, 0, 0, 10,   0,  10],
    [-50, -75,  0, 0, 0,  0, -75, -50],
    [100, -50, 10, 5, 5, 10, -50, 100]
]

# mettre commentaire
def get_best_move(list_moves):
    best_move = None
    best = float('-inf')
    for elem in list_moves:
        coo = get_coordinates(elem)
        x = coo[0]
        y = coo[1]
        value = Tactic_Mtx[x][y]
        if value > best:
            best = value
            best_move = elem
    return best_move

#
def get_count_pawn(board):
    nb_black = len(board[0])
    nb_white = len(board[1])
    return (nb_black, nb_white)

# list_score = []
#         list_moves = legal_moves(board, current)
#         for move in list_moves:
#             score = get_score(move)
#             list_score.append(score)
#         return list_score
# mettre commentaire


def minmax(board, current, depth):
    if depth == 0:
        nb_black, nb_white = get_count_pawn(board)
        return nb_black-nb_white

    if current == 0:
        best_move = None
        max_score = float('-inf')
        list_moves = legal_moves(board, 0)
        for move in range(len(list_moves)):
            new_board = newboard(board, list_moves[move], 0)
            score = minmax(new_board, 1, depth-1)
            if max_score < score:
                max_score = max(max_score, score)
                best_move = list_moves[move] # de la 1ère list_moves
        print('best_moves ==> ', best_move)
        return best_move

    else:
        best_move = None
        min_score = float('inf')
        list_moves = legal_moves(board, 1)
        for move in range(len(list_moves)):
            new_board = newboard(board, list_moves[move], 1)
            score = minmax(new_board, 0, depth-1)
            if min_score > score:
                min_score = min(min_score, score)
                best_move = list_moves[move]
        print('min_score ==> ', best_move)
        return best_move

# donne le score
def get_score(index):
    coo = get_coordinates(index)
    row = coo[0]
    col = coo[1]
    score = Tactic_Mtx[row][col]
    return score


### FAIRE SON TEST ###
# IA qui retourne le meilleur coup à jouer
# def minimax(board, list_moves, current, depth):
#     if depth == 0:
#         # on retourne la différence de best_moves(current=1) - best_moves(current=0)
#         return "FINI"
#
#
#
#     if current == 0:
#         best = float('-inf')
#         for move in list_moves:
#             print(move)
#             new_board = newboard(board, move, current)
#             coo = get_coordinates(move)
#             x = coo[0]
#             y = coo[1]
#             value = Tactic_Mtx[x][y]
#             best = minimax(new_board , current, depth - 1)
#             best_move = max(value, best)
#         return best_move
#
#     else:
#         best_score = float('inf')
#         for move in list_moves:
#             new_board = newboard(board, move, current)
#             score = minimax(new_board, current, depth - 1)
#             best_score = max(best_score, score)
#         return best_score


### FAIRE SON TEST ###
# donne la nouvelle board possible pour chaque coup envisageable
def newboard(board, move, current):
    '''
    :param board: la board précédente
    :param move: le coup pour lequel on veut vérifier
    :param current: savoir si c'est pour les noirs ou les blancs
    :return: la nouvelle board
    '''
    myColor = set(board[current])
    otherColor = set(board[abs(current - 1)])
    for list in list_directions(move):
        listOtherColor = set()
        for cell in list:
            if cell in otherColor:
                listOtherColor.add(cell)
            elif cell in myColor:
                if len(listOtherColor) > 0:
                    myColor = myColor.union(listOtherColor)
                    otherColor = [x for x in otherColor if (x not in listOtherColor)]
            else:
                break
    myColor.add(move)
    if current == 0:
        newboard= [sorted(myColor), otherColor]
    else:
        newboard= [otherColor, sorted(myColor)]
    return newboard


# board = [[35, 36, 44, 45], [20, 27, 28, 37, 46, 55]]
# list_moves = [12, 18, 19, 21, 29, 30, 38, 47]
# move = minimax(list_moves, 0)
# '''move = 18'''
# newboard(board, move, 0)
# # newboard = [[18, 27, 35, 36, 44, 45], [20, 28, 37, 46, 55]]

board = [[28, 35], [27, 36]]
depth = 2
current = 0

print(minmax(board, current, depth))
#  newboard = [[26, 27, 28, 35], [36]]