from board import Board
class Game_logic:
    def __init__(self,):
        self.player1 = "X"
        self.player2 = "O"
        self.move_count = 0
        self.board = Board()

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

    # this method will ask user to enter their move
    def get_user_input(self):
        print('Please write your next move here as ROW NUMBER(0-2) COMMA COLUMN NUMBER(0-2), example: 1,2')
        while True:
            user_input = input('Your next move is: ')
            if user_input.count(",") == 1:
                row, col = user_input.split(",")
                if row.isdigit() and 0 <= int(row) <= 2 and col.isdigit() and 0 <= int(col) <= 2:
                    return int(row), int(col)
            print("Invalid input, try again.")

    # this will determine who's turn it is
    def next_move(self):
        while True:
            player = self.player1 if self.move_count % 2 == 0 else self.player2
            # call the user input method
            row, col = self.get_user_input()
            if self.board[row][col] == " ":
                self.board[row][col] = player
                self.move_count += 1     # the purpose of this is to count the moves
                print("Current board: ")
                print(self.board)
                break
            else:
                print("This move is already taken, try again.")