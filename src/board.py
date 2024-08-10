class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

# # Removed this method as it was too complicated to check for wins, might add it back later
#     def make_board(self, rows, cols, value=None):
#         self.rows = rows
#         self.cols = cols
#         self.board = [[value for _ in range(cols)] for _ in range(rows)]


    def display_board(self):
        for collection in self.board:
            for x in collection:
                print(x, end="|")
            print()