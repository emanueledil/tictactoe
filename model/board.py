
from model.mark import MAP_WIN, MARK
from constants import DIGITS_TO_POSITION

class Board:
    def __init__(self):
        self.clean_board()

    def clean_board(self):
        self.board = [[MARK.EMPTY for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print("|".join(mark.value for mark in row))
            print("-" * 5)
        print("#"*10)    

    def put_mark_by_digit(self, digit: int, mark: MARK)-> bool:
        row, col = DIGITS_TO_POSITION.get(digit, None)
        if row is None or col is None:
            return False
        if self.board[row][col] != MARK.EMPTY:
            return False
        self._put_mark(mark, row, col)
        return True

    def _put_mark(self, mark: MARK, row: int, col: int)-> bool:
        self.board[row][col] = mark


    def check_winner(self):
        for mark in [MARK.O, MARK.X]:
            if self._check_win_horizontal(mark):
                return True
            if self._check_win_vertical(mark):
                return True
            if self._check_win_diagonal(mark): 
                return True
        return False
                
    def _check_win_horizontal(self, mark: MARK):
        for row_index, row in enumerate(self.board):
            if row.count(mark) == 3:
                [self._put_mark(MAP_WIN.get(mark), row_index, i) for i in range(3)]
                return True
        return False
    
    def _check_win_vertical(self, mark: MARK):
        for column_index in range(3):
            if self._is_column_winner(column_index, mark):
                return True
        return False
    
    def _check_win_diagonal(self, mark: MARK):
        main_diagonal = [self.board[i][i] for i in range(3)]
        if main_diagonal.count == 3:
            [self._put_mark(MAP_WIN.get(mark), i, i)  for i in range(3)]
            return True
        anti_diagonal = [self.board[i][2-i] for i in range(3)]
        if anti_diagonal.count == 3:
            [self._put_mark(MAP_WIN.get(mark), i, 2-i)  for i in range(3)]
            return True
        return False

    def _is_column_winner(self, col_index: int, mark: MARK):
        output_col = []
        for row in self.board:
            output_col.append(row[col_index])
        if output_col.count(mark) == 3:
            [self._put_mark(MAP_WIN.get(mark), i, col_index) for i in range(3)]
            return True
        return False



