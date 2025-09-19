
from exceptions.board_exceptions import BoxAlreadyFilled
from model.mark import MAP_WIN, MARK
from constants import DIGITS_TO_POSITION

class Board:
    """Core component of the game.

    Handles user input, rendering, and logic.
    """
    def __init__(self):
        self.clean_board()

    def clean_board(self):
        """Initialize or reset the board to an empty state."""
        self._board = [[MARK.EMPTY for _ in range(3)] for _ in range(3)]

    def display(self):
        """Display the current state of the board."""
        for row_index, row in enumerate(self._board):
            print("|".join(mark.value for mark in row))
            if row_index<2:
                print("-" * 5)  

    def put_mark_by_digit(self, digit: int, mark: MARK)-> bool:
        """Put a mark on the board based on a digit from 1 to 9."""
        row, col = DIGITS_TO_POSITION.get(digit, None)
        if row is None or col is None:
            return False
        if self._board[row][col] != MARK.EMPTY:
            raise BoxAlreadyFilled()
        self._put_mark(mark, row, col)
        return True

    def _put_mark(self, mark: MARK, row: int, col: int)-> bool:
        """Put a mark on the board at the specified row and column."""
        self._board[row][col] = mark


    def check_winner(self):
        """Check if there's a winner on the board."""
        for mark in [MARK.O, MARK.X]:
            if self._check_win_horizontal(mark):
                return True
            if self._check_win_vertical(mark):
                return True
            if self._check_win_diagonal(mark): 
                return True
        return False
                
    def _check_win_horizontal(self, mark: MARK):
        """Check all rows for a win."""
        for row_index, row in enumerate(self._board):
            if row.count(mark) == 3:
                [self._put_mark(MAP_WIN.get(mark), row_index, i) for i in range(3)]
                return True
        return False
    
    def _check_win_vertical(self, mark: MARK):
        """Check all columns for a win."""
        for column_index in range(3):
            if self._is_column_winner(column_index, mark):
                return True
        return False
    
    def _check_win_diagonal(self, mark: MARK):
        """Check both diagonals for a win."""
        main_diagonal = [self._board[i][i] for i in range(3)]
        if main_diagonal.count == 3:
            [self._put_mark(MAP_WIN.get(mark), i, i)  for i in range(3)]
            return True
        anti_diagonal = [self._board[i][2-i] for i in range(3)]
        if anti_diagonal.count == 3:
            [self._put_mark(MAP_WIN.get(mark), i, 2-i)  for i in range(3)]
            return True
        return False

    def _is_column_winner(self, col_index: int, mark: MARK):
        """Check if a single column is filled with the same mark."""
        for row in self._board:
            if row[col_index] != mark:
                return False
        [self._put_mark(MAP_WIN.get(mark), i, col_index) for i in range(3)]
        return True
    
    def is_full(self):
        """Check if the board is full."""
        for row in self._board:
            if MARK.EMPTY in row:
                return False
        return True
