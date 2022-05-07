from strategies import *

def test_get_Weight():
    assert get_Weight(0) == 100
    assert get_Weight(1) == -50


def test_weight_strategy():
    assert weight_strategy([0, 15, 30, 42]) == 0


def test_play_move():
    assert play_move([[28, 35], [27, 36]], 44, 0) == [[35, 28, 36, 44], [27]]
    assert play_move([[35, 28, 36, 44], [27]], 29, 1) == [[35, 36, 44], [27, 28, 29]]


def test_evaluation():
    assert evaluation([[28, 35], [27, 36]], 0) == 0
    assert evaluation([[0, 28, 35], [27, 36]], 0) == 100
    assert evaluation([[28, 35], [0, 27, 36]], 0) == -100

