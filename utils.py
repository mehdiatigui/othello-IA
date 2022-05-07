directions = [
    (0, -1),  # Up
    (1, -1),  # Up-Right
    (1, 0),  # Right
    (1, 1),  # Down-Right
    (0, 1),  # Down
    (-1, 1),  # Down-Left
    (-1, 0),  # Left
    (-1, -1),  # Up-Left
]


# BOARD
# 00 01 02 03 04 05 06 07
# 08 09 10 11 12 13 14 15
# 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30 31
# 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47
# 48 49 50 51 52 53 54 55
# 56 57 58 59 60 61 62 63

# Vérifier si les coordonnées sont à l'intérieur du plateau 8*8
def is_inside(row, col):
    '''
    :param row: ligne
    :param col: colonne
    :return boolean: True si row et col sont à l'intérieur du board
    '''
    return 0 <= row < 8 and 0 <= col < 8


# Retourner les coordonnées row, col à partir d'un numéro index
def get_coordinates(index):
    '''
    :param index: l'index de la case (entre 0 et 63)
    :return: les coordonnées à partir de l'index
    '''
    return index // 8, index % 8


# Retourner un index entre 0 et 63 à partir des coordonnées row, col
def get_index(row, col):
    '''
    :param row: ligne
    :param col: colonne
    :return: l'index sur le board
    '''
    return row * 8 + col


# retourner True si l'index dans le board est un corner
def isCorner(index):
    if index in [0, 7, 56, 63]:
        return True
    return False


# Vérifier si une liste de possibilité contient un corner, si oui le retourner
def getCorner(legalMoves_list):
    corner = list({*[0, 7, 56, 63]} & {*legalMoves_list})
    return corner


# retourner le nombre de cases vides
def get_count_empty(board):
    return 64 - (len(board[0]) + len(board[1]))


def isGameOver(board):
    # Si aucun coup n'est possible pour les joueurs, gameOver
    black_legal_moves = get_legal_moves(board, 0)
    white_legal_moves = get_legal_moves(board, 1)
    if black_legal_moves or white_legal_moves:
        return False
    return True


# retourner la prochaine case en suivant une direction
def avancer(tile, direction):
    currentTile = tile
    row, col = get_coordinates(currentTile)
    while is_inside(row + direction[0], col + direction[1]):
        row = row + direction[0]
        col = col + direction[1]
        currentTile = get_index(row, col)
        yield currentTile


# Retourner les listes des index dans les 8 directions possibles
def list_directions(index):
    '''
    :param index : nombre (compris entre 0 et 63)
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


# Retourner la liste de coups possibles pour le joueur current
def get_legal_moves(board, playerIndex):
    '''
    :param board: liste contenant les deux listes des index des joueurs
    :param current: l'index dujoueur ? 0 ou 1
    :return: une liste de coups possibles
    '''
    otherPlayerIndex = abs(playerIndex - 1)  # (playerIndex + 1) % 2
    legalMoves = set()

    playerColors = board[playerIndex]
    otherPlayerColors = board[otherPlayerIndex]

    for elem in playerColors:
        for list in list_directions(elem):
            listOtherColor = []

            for cell in list:
                # si case de couleur différente ==> ajouter à la liste
                if cell in otherPlayerColors:
                    listOtherColor.append(cell)
                # si de meme couleur, arréter
                elif cell in playerColors:
                    break
                # sinon, la case est vide.
                else:
                    if len(listOtherColor) > 0:
                        legalMoves.add(cell)
                    break
    return legalMoves