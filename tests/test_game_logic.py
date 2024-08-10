import unittest
from game_logic import Game_logic

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        """Set up the game board for testing."""
        self.game = Game_logic()

    def test_wins_hor(self):
        """Test the game board for horizontal wins."""
        self.game.board.board = [
            ["X", "X", "X"],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.assertTrue(self.game.check_for_win())

    def test_wins_ver(self):
        """Test the game board for vertical wins."""
        self.game.board.board = [
            ["X", " ", " "],
            ["X", " ", " "],
            ["X", " ", " "]
        ]

        self.assertTrue(self.game.check_for_win())

    def test_diagonal_win(self):
        """Test that a diagonal win is correctly identified."""
        self.game.board.board = [
            ["X", " ", " "],
            [" ", "X", " "],
            [" ", " ", "X"]
        ]

        self.assertTrue(self.game.check_for_win())

if __name__ == '__main__':
    unittest.main()