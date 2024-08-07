from board import Board
class Game_logic:
    def __init__(self,):
        self.player1 = "X"
        self.player2 = "O"

    def check_for_win(self,current_board):
        players_list = current_board
        winner = None
        # Check rows
        if players_list[0][0] == players_list[0][1] == players_list[0][2] != " ":
            winner = players_list[0][0]
        if players_list[1][0] == players_list[1][1] == players_list[1][2] != " ":
            winner = players_list[1][0]
        if players_list[2][0] == players_list[2][1] == players_list[2][2] != " ":
            winner = players_list[2][0]
        # Check columns
        if players_list[0][0] == players_list[1][0] == players_list[2][0] != " ":
            winner = players_list[0][0]
        if players_list[0][1] == players_list[1][1] == players_list[2][1] != " ":
            winner = players_list[0][1]
        if players_list[0][2] == players_list[1][2] == players_list[2][2] != " ":
            winner = players_list[0][2]
        # Check diagonals
        if players_list[0][0] == players_list[1][1] == players_list[2][2] != " ":
            winner = players_list[0][0]
        if players_list[0][2] == players_list[1][1] == players_list[2][0] != " ":
            winner = players_list[0][2]
        print("Today's winner is ", winner)

    def check_for_tie(self, current_board):
        for row in current_board:
            if ' ' in row:
                return False
        print("It's a tie!")
        return True

    def next_move(self,current_board):
        p1 = "X"
        p2 = "O"
        while True:
            player = p1 if current_board.count(" ") % 2 == 1 else p2
            move = input("Next move for player " + player + " (0-8): ")
            if move.isdigit() and 0 <= int(move) <= 8 and current_board[int(move)] == " ":
                current_board[int(move)] = player
                break
            else:
                print("Invalid move, try again.")