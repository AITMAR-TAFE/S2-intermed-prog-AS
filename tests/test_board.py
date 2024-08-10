import unittest
from board import Board
import io
import sys

class TestBoard(unittest.TestCase):

    def setUp(self):
        """Set up the board for testing."""
        self.board = Board()
        self.board.board = [[" " for _ in range(3)] for _ in range(3)]

    def test_initial_board(self):
        """Test that the board initializes to a 3x3 grid of empty spaces."""
        expected_board = [[" " for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.board.board, expected_board)


if __name__ == '__main__':
    unittest.main()
