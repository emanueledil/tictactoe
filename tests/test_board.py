import pytest

from model.board import Board
from model.mark import MARK
from exceptions.board_exceptions import BoxAlreadyFilled


def test_put_mark_by_digit_places_mark():
    board = Board()
    ok = board.put_mark_by_digit(5, MARK.X)
    assert ok is True

def test_put_mark_by_digit_on_filled_box_raises():
    board = Board()
    board.put_mark_by_digit(5, MARK.X)
    with pytest.raises(BoxAlreadyFilled):
        board.put_mark_by_digit(5, MARK.O)


@pytest.mark.parametrize(
        ["moves", "expected"],
        [((1,2,3), True), 
         ((1,5,9), True), 
         ((7,5,3), True), 
         ((8,5,2), True),
         ((5,1,2), False),
         ((7,8,3), False),
         ]
)
def test_win(moves, expected):
    board = Board()

    for move in moves:
        assert board.check_winner() is False
        board.put_mark_by_digit(move, MARK.X)
    assert board.check_winner() is expected

