from exceptions.board_exceptions import BoxAlreadyFilled
from model.board import Board
from model.mark import MARK

def get_player_input()-> int:
    while True:
        try:
            move = int(input("Insert a number from 1 to 9: "))
            if 1 <= move <= 9:
                return move
            else:
                print("Only numbers from 1 to 9 are allowed")
        except ValueError:
            print("Only numbers from 1 to 9 are allowed")

def place_mark(board: Board, mark: MARK):
    while True:
        try:
            move = get_player_input()
            board.put_mark_by_digit(move, mark)
            break
        except BoxAlreadyFilled:
            print("Box already filled, choose another one")

def main():
    board = Board()
    board.display()
    x_player_turn = True

    while True:
        player_mark = MARK.X if x_player_turn else MARK.O
        print(f"##### {player_mark.value}'s turn #####")
        place_mark(board, player_mark)
        win = board.check_winner()
        board.display()
        if board.is_full() and not win:
            print("##### It's a draw! #####")
            break
        if win:
            print(f"##### {player_mark.value} wins! #####")
            break
        x_player_turn = not x_player_turn


if __name__ == "__main__":
    main()
