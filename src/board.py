class Board:
    def __init__(self):
        self.board = []

    def make_board(self,rows,cols, value=None):
        self.rows = rows
        self.cols = cols
        self.board = [[value for _ in range(cols)] for _ in range(rows)]

    def display_board(self):
        for collection in self.board:
            for x in collection:
                print(x, end="|")
            print()