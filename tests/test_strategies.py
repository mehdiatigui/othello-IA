from strategies import *


def test_random_strategy():
    random.seed(5)
    assert random_strategy([45, 14, 12, 0]) == (12, 'random :12')
    assert random_strategy([]) == (None, 'None')


def test_get_Weight():
    assert get_Weight(0) == 100
    assert get_Weight(1) == -50


def test_sorting_legal_moves_weighted():
    assert sorting_legal_moves_weighted([37, 8, 19, 21, 53]) == [21, 37, 19, 53, 8]


def test_weight_strategy():
    assert weight_strategy([0, 15, 30, 42]) == 0


def test_play_move():
    assert play_move([[28, 35], [27, 36]], 44, 0) == [[35, 28, 36, 44], [27]]
    assert play_move([[35, 28, 36, 44], [27]], 29, 1) == [[35, 36, 44], [27, 28, 29]]


def test_update_weight_value():
    update_weight_value([[0, 7, 56, 63], []], 0)
    update_weight_value([[], [0, 7, 56, 63]], 0)


def test_change_weight_value():
    new_weight = 150
    change_weight_value([1, 8, 9], new_weight)
    change_weight_value([6, 14, 15], new_weight)
    change_weight_value([48, 49, 57], new_weight)
    change_weight_value([54, 55, 63], new_weight)
    new_weight = 0
    change_weight_value([2, 16], new_weight)
    change_weight_value([5, 23], new_weight)
    change_weight_value([48, 58], new_weight)
    change_weight_value([61, 47], new_weight)


def test_evaluation():
    assert evaluation([[28, 35], [27, 36]], 0) == 0
    assert evaluation([[0, 28, 35], [27, 36]], 0) == 100
    assert evaluation([[28, 35], [0, 27, 36]], 0) == -100


def test_minimax_strategy():
    # Aucune possibilité dans la liste legal_moves
    assert minimax_strategy([[28, 35], [27, 36]], [], 0) == (None, 'Je joue None en 0.00 secondes')

    # Une seule possibilité
    assert minimax_strategy([[16, 3, 0, 9, 2, 1, 10, 8, 26, 17, 40, 61, 56, 48, 19, 35, 28, 49, 63, 27, 20, 21, 57, 47,
                              55, 45, 54, 59, 51, 58, 24, 25, 32, 33, 42, 62, 63, 44, 7, 31, 15, 39, 23, 6, 4, 5],
                             [41, 34, 50, 11, 18, 36, 22, 43, 29, 60, 52, 37, 38, 46, 53, 14, 12, 13]],
                            [30], 0) == (30, 'Je joue 30 en 0.00 secondes')

    # Un coin se trouve dans la liste legal_moves
    assert minimax_strategy([[41, 40, 33, 42, 34, 35, 14, 21, 55, 46, 62, 44, 53, 30, 37, 38],
                             [27, 2, 10, 18, 16, 17, 26, 45, 36, 29, 28]],
                            [32, 39, 7, 43, 13, 47, 48, 49, 50, 52, 61, 31], 1) == (7, 'Je joue 7 en 0.00 secondes')

    # Si la recherche minimax n'a pas abouti en 9.5 secondes
    minimax_strategy([[26, 42, 34, 45, 61, 52, 10, 18, 37, 35], [20, 28, 44, 27, 51, 43, 29, 36]],
                     [12, 13, 50, 19, 21, 53, 58, 59, 60, 30], 0)


def test_minimax():
    assert minimax(0, [[27, 26, 35, 28], [36]], 3, False, -1000000, 1000000) == -10
    # si liste legal_Moves est vide
    # pour mon joueur
    assert minimax(0, [
        [0, 1, 8, 9, 10, 17, 19, 25, 26, 28, 33, 35, 41, 42, 43, 44, 49, 50, 51, 52, 53, 57, 58, 59, 60, 61, 62],
        [2, 3, 4, 5, 6, 11, 12, 13, 16, 18, 20, 21, 22, 23, 24, 27, 29, 30, 31, 32, 34, 36, 37, 38, 39, 40, 45, 46, 47,
         48, 54, 55, 56, 63]],
                   3, False, -1000000, 1000000) == 652
    # pour l'autre joueur
    assert minimax(1, [
        [0, 1, 8, 9, 10, 17, 19, 25, 26, 28, 33, 35, 41, 42, 43, 44, 49, 50, 51, 52, 53, 57, 58, 59, 60, 61, 62],
        [2, 3, 4, 5, 6, 11, 12, 13, 16, 18, 20, 21, 22, 23, 24, 27, 29, 30, 31, 32, 34, 36, 37, 38, 39, 40, 45, 46, 47,
         48, 54, 55, 56, 63]],
                   3, True, -1000000, 1000000) == -652
