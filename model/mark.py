from enum import Enum

class MARK(Enum):
    X = "x"
    O = "o"
    EMPTY = " "

    X_WIN = "#"
    O_WIN = "@"

MAP_WIN = {
    MARK.X: MARK.X_WIN,
    MARK.O: MARK.O_WIN,
    MARK.EMPTY: MARK.EMPTY
}