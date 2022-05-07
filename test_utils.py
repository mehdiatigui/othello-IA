from utils import *

def test_is_inside():
    assert is_inside(8, 1) == False
    assert is_inside(3, 5) == True


def test_get_coordinates():
    assert get_coordinates(15) == (1, 7)


def test_get_index():
    assert get_index(3, 2) == 26


def test_isCorner():
    assert isCorner(9) == False
    assert isCorner(0) == True


def test_getCorner():
    assert getCorner([19, 26, 37, 44]) == []
    assert getCorner([0, 19, 26, 37, 44]) == [0]


def test_get_count_empty():
    assert get_count_empty([[28, 35], [27, 36]]) == 60


def test_isGameOver():
    assert isGameOver([[28, 35], [27, 36]]) == False
    assert isGameOver([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                        11, 12, 13, 14, 15, 16, 18, 19, 20,
                        21, 23, 24, 25, 27, 28, 30, 31, 32,
                        33, 34, 35, 36, 38, 39, 40, 41, 42,
                        43, 44, 46, 47, 48, 49, 50, 51, 53,
                        54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
                       [17, 22, 26, 29, 37, 45, 52]]) == True


def test_list_directions():
    # assert list_directions(26) == []
    pass

def test_get_legal_moves():
    assert get_legal_moves([[28, 35], [27, 6]], 0) == {19, 26}
