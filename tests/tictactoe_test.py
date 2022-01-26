import unittest
import tictactoe


class TestMarkSquare(unittest.TestCase):

    def test_new_square(self):
        board = tictactoe.Board()
        column = row = 0
        player = 'X'

        self.assertTrue(board.mark_square(row, column, player))

    def test_full_square(self):
        board = tictactoe.Board()
        column = row = 0
        player = 'X'

        board.mark_square(column, row, player)

        self.assertFalse(board.mark_square(row, column, player))

    def test_out_of_bounds_square(self):
        board = tictactoe.Board()
        column = row = 4
        player = 'X'

        self.assertFalse(board.mark_square(row, column, player))


class TestChangePlayer(unittest.TestCase):

    def test_no_player_init(self):
        board = tictactoe.Board()
        board.change_player()

        self.assertEqual(board.__current_player, 'O')

    def test_change_O_to_X(self):
        board = tictactoe.Board()
        board.change_player()
        board.change_player()

        self.assertEqual(board.__current_player, 'X')

    def test_change_X_to_O(self):
        board = tictactoe.Board()
        board.change_player()
        board.change_player()
        board.change_player()

        self.assertEqual(board.__current_player, 'O')
