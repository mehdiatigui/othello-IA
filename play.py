import random

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

### FAIRE UN TEST ?
def play(msg):
    board = msg['state']['board']
    current = msg['state']['current']
    try:
        legalMoves = legal_moves(board, current)
        move = random.choice(legalMoves)
        move = int(move)
    except:
        move = None

    message = {
        "response": "move",
        "move": move,
        "message": str(move)
    }
    return message


def get_coordinates(index):
    '''
    :param index:
    :return:
    '''
    row = index // 8
    col = index % 8
    return row, col


def is_inside(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True


def get_index(row, col):
    return row * 8 + col


### FAIRE SON TEST ###
def list_directions(index):
    for dir in directions:
        list = []
        row, col = get_coordinates(index)
        while is_inside(row, col):
            row += dir[0]
            col += dir[1]
            list.append(get_index(row, col))
        list.pop()
        yield list


def legal_moves(board, current):
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

