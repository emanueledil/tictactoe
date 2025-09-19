# Basic Tictactoe

This is a basic excercise for practicing clean code practices
It's a tictactoe CLI game in which the user can input the position of the marker in the same position on the numeric keypad (1 on the bottom left)

When a win is detected, the marked signs of the winner are changed (x->#, o->@) to signal the winning position

## Requirements
```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```


## How to run 

`python3 main.py`

Then it is asked alternatively to the players to put their number which correspond to the position in which they want to put their mark.
The script ends when one of the two players win or if they draw

## exceptions
In this simple example only an exception in case of placing a marker over another one is implemented. 
The exceptions are kept in a separated folder

## model
The Board class is the main component of this repo. It manages logic, rendering and user input.
The rest of the logic is handled in the main function, with a loop that alternates between the inputs of the two players, which are represented by an enum for their marker sign. In case of victory the enum is mapped to a different sign, to signal it.
At the base of the repo, in the constants file, a map for the board position from the numeric input is provided

## Tests
```bash
source .env/bin/activate
pytest .
```
