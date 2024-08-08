from board import Board
from game_logic import Game_logic

obj1 = Board()
obj1.board[0][0] = "X"
obj1.board[0][1] = "X"
obj1.board[0][2] = "X"

obj1.display_board()
print(obj1.board)

game = Game_logic()
game.check_for_win(obj1.board)
game.check_for_tie(obj1.board)
input1 = game.get_user_input()
print(input1)
game.next_move()