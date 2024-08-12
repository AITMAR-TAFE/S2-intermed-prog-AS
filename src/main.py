from game_logic import Game_logic
print("Welcome to my tic-tac-toe game!")
print("The game rules are: players take turns placing Xs and Os on a 3x3 grid; the first to get three in a row wins.\nIf the grid fills up with no winner, it’s a tie.")
print("To write your next move follow this -  ROW NUMBER(0-2) COMMA COLUMN NUMBER(0-2), example: 1,2")
obj1 = Game_logic()
obj1.next_move()

