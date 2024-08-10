from board import Board
class Game_logic():
    def __init__(self):
        # Initializing the game with a new board and default player symbols
        self.board = Board()
        self.player1 = "X"
        self.player2 = "O"
        self.move_count = 0

    def check_for_win(self):
        # Check if there is a winner.
        players_list = self.board.board
        winner = None
        # Check rows and columns
        for i in range(3):
            if players_list[i][0] == players_list[i][1] == players_list[i][2] != " ":
                winner = players_list[i][0]
            if players_list[0][i] == players_list[1][i] == players_list[2][i] != " ":
                winner = players_list[0][i]

        # Check diagonals
        if players_list[0][0] == players_list[1][1] == players_list[2][2] != " ":
            winner = players_list[0][0]
        if players_list[0][2] == players_list[1][1] == players_list[2][0] != " ":
            winner = players_list[0][2]

        if winner:
            print("Today's winner is ", winner)

    def check_for_tie(self):
        # Checks is there is any empty space on board for playing
        for row in self.board.board:
            if ' ' in row:
                return False
        print("It's a tie!")
        return True

    def get_user_input(self):
        # Ask user for next move
        print('Please write your next move here as ROW NUMBER(0-2) COMMA COLUMN NUMBER(0-2), example: 1,2')
        while True:
            user_input = input('Your next move is: ')
            if user_input.count(",") == 1:
                row, col = user_input.split(",")
                if row.isdigit() and 0 <= int(row) <= 2 and col.isdigit() and 0 <= int(col) <= 2:
                    return int(row), int(col)
            print("Invalid input, try again.")

    def next_move(self):
        # This method will tell who's turn it is
        while True:
            player = self.player1 if self.move_count % 2 == 0 else self.player2
            # call the user input method
            row, col = self.get_user_input()

            if self.board.board[row][col] == " ":
                self.board.board[row][col] = player
                self.move_count += 1     # the purpose of this is to count the moves
                print("Current board: ")
                self.board.display_board()
                if self.check_for_win():
                    break
                if self.check_for_tie():
                    break
            else:
                print("This move is already taken, try again.")