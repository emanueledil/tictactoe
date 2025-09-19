
from model.mark import MARK


class Board:
    def __init__(self):
        self.board = [[MARK.EMPTY for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print("|".join(mark.value for mark in row))
            print("-" * 5)
