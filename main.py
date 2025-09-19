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

def main():
    board = Board()
    board.display()
    x_player_turn = True

    while True:
        player_mark = MARK.X if x_player_turn else MARK.O
        print(f"##### {player_mark.value}'s turn #####")
        move = get_player_input()
        board.put_mark_by_digit(move, player_mark)
        board.check_winner()
        board.display()
        x_player_turn = not x_player_turn


if __name__ == "__main__":
    main()
