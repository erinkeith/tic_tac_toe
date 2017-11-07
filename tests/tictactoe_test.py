import unittest
import tictactoe


class TestMarkSquare(unittest.TestCase):

    def test_new_square(self):
        board = tictactoe.Board()
        column = row = 0
        player = 'X'

        self.assertTrue(board.mark_square(column, row, player))

    def test_full_square(self):
        board = tictactoe.Board()
        column = row = 0
        player = 'X'

        board.mark_square(column, row, player)

        self.assertFalse(board.mark_square(column, row, player))

    def test_out_of_bounds_square(self):
        board = tictactoe.Board()
        column = row = 4
        player = 'X'

        self.assertFalse(board.mark_square(column, row, player))