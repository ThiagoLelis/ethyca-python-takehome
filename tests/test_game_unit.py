import unittest
import json
from app import app
from api.game_logic import TicTacToeGame

class TestGameUnit(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_check_winner(self):
        game = TicTacToeGame()
        game.board = [['X', 'O', 'X'],
                      [' ', 'X', 'O'],
                      ['O', ' ', 'X']]

        is_winner, winner = game.check_winner()

        self.assertTrue(is_winner)
        self.assertEqual(winner, 'X')


    def test_check_winner_no_winner(self):
        game = TicTacToeGame()
        game.board = [['X', 'O', 'X'],
                      [' ', 'X', 'O'],
                      ['O', ' ', 'O']]

        is_winner, winner = game.check_winner()

        self.assertFalse(is_winner)
        self.assertIsNone(winner)

    def test_check_winner_row(self):
        game = TicTacToeGame()
        game.board = [['X', 'X', 'X'],
                      [' ', 'O', 'O'],
                      ['O', ' ', 'X']]

        is_winner, winner = game.check_winner()

        self.assertTrue(is_winner)
        self.assertEqual(winner, 'X')

    def test_check_winner_column(self):
        game = TicTacToeGame()
        game.board = [['X', 'O', 'X'],
                      ['X', 'O', 'O'],
                      ['X', ' ', 'X']]

        is_winner, winner = game.check_winner()

        self.assertTrue(is_winner)
        self.assertEqual(winner, 'X')

    def test_check_draw(self):
        game = TicTacToeGame()
        game.board = [['X', 'O', 'X'],
                      ['X', 'O', 'O'],
                      ['O', 'X', 'X']]

        is_winner, winner = game.check_winner()

        self.assertTrue(is_winner)
        self.assertEqual(winner, 'Draw')


if __name__ == '__main__':
    unittest.main()
