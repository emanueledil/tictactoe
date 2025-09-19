from model.board import Board
from model.mark import MARK

def main():
    board = Board()
    board.display()
    board.put_mark_by_digit(5, MARK.X)
    board.put_mark_by_digit(4, MARK.X)
    board.put_mark_by_digit(6, MARK.X)
    board.check_winner()
    board.display()

if __name__ == "__main__":
    main()
