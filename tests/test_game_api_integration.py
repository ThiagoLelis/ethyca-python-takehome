import unittest
from app import app
from unittest.mock import patch

from api.game_logic import TicTacToeGame


class TestGameApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    @patch("api.game_services.games", {})
    def test_create_game(self):
        response = self.app.post("/api/v1/games")
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Game created successfully")
        self.assertTrue(data["game_id"] == 1)

    @patch("api.game_services.games", {})
    def test_create_large_game(self):
        response = self.app.post("/api/v1/games", json={"board_type": "large"})
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Game created successfully")
        self.assertTrue(data["game_id"] == 1)

    @patch("api.game_services.games", {})
    def test_create_huge_game(self):
        response = self.app.post("/api/v1/games", json={"board_type": "huge"})
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Game created successfully")
        self.assertTrue(data["game_id"] == 1)

    def test_create_move(self):
        response = self.app.post("/api/v1/games")
        game_id = response.get_json()["game_id"]

        response = self.app.post(
            f"/api/v1/games/{game_id}/moves", json={"x": 1, "y": 1}
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Move created successfully")
        self.assertEqual(len(data["board"]), 3)
        self.assertEqual(len(data["board"][0]), 3)
        self.assertEqual(data["board"][1][1], "X")
        self.assertTrue(any("O" in row for row in data["board"]))

    def test_create_with_none_coordinates(self):
        response = self.app.post("/api/v1/games")
        game_id = response.get_json()["game_id"]

        response = self.app.post(
            f"/api/v1/games/{game_id}/moves", json={"x": None, "y": None}
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "Invalid coordinates")

    @patch("api.game_services.games", {})
    def test_create_move_with_invalid_game_id(self):
        response = self.app.post("/api/v1/games/1/moves", json={"x": 1, "y": 1})
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Game not found")

    def test_create_invalid_move(self):
        response = self.app.post("/api/v1/games")
        game_id = response.get_json()["game_id"]

        response = self.app.post(
            f"/api/v1/games/{game_id}/moves", json={"x": 1, "y": 1}
        )
        response = self.app.post(
            f"/api/v1/games/{game_id}/moves", json={"x": 1, "y": 1}
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "Invalid move")

    def test_create_move_out_of_bounds(self):
        response = self.app.post("/api/v1/games")
        game_id = response.get_json()["game_id"]

        response = self.app.post(
            f"/api/v1/games/{game_id}/moves", json={"x": 4, "y": 4}
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "Coordinates out of bounds")

    @patch("api.game_services.games", {})
    def test_get_games(self):
        self.app.post("/api/v1/games")
        self.app.post("/api/v1/games")
        self.app.post("/api/v1/games")

        response = self.app.get("/api/v1/games")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data["games"]), 3)
        self.assertTrue(data["games"][0]["game_id"] == 1)
        self.assertTrue(data["games"][1]["game_id"] == 2)
        self.assertTrue(data["games"][2]["game_id"] == 3)

    game = TicTacToeGame()
    game.moves = [
        {"id": 1, "player": "X", "x": 1, "y": 1},
        {"id": 3, "player": "X", "x": 0, "y": 1},
        {"id": 2, "player": "O", "x": 2, "y": 2},
    ]

    @patch("api.game_services.games", {1: game})
    def test_get_moves(self):
        response = self.app.get(f"/api/v1/games/1/moves")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data["moves"]), 3)
        self.assertTrue(data["game_id"] == 1)
        self.assertTrue(data["moves"][0] == {"id": 1, "player": "X", "x": 1, "y": 1})
        self.assertTrue(data["moves"][1] == {"id": 2, "player": "O", "x": 2, "y": 2})
        self.assertTrue(data["moves"][2] == {"id": 3, "player": "X", "x": 0, "y": 1})

    @patch("api.game_services.games", {})
    def test_get_move_with_invalid_game_id(self):
        response = self.app.get("/api/v1/games/1/moves")
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Game not found")

    game = TicTacToeGame()
    game.board = [["X", " ", "X"], ["X", "O", "O"], ["O", " ", "X"]]

    @patch("api.game_services.games", {1: game})
    def test_create_winner_move(self):
        response = self.app.post(f"/api/v1/games/1/moves", json={"x": 0, "y": 1})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Player X won")
        self.assertEqual(
            data["board"], [["X", "X", "X"], ["X", "O", "O"], ["O", " ", "X"]]
        )

    game = TicTacToeGame()
    game.board = [["X", " ", "O"], ["X", "O", "X"], ["O", " ", "O"]]

    @patch("api.game_services.games", {1: game})
    def test_create_lost_winner_move(self):
        response = self.app.post(f"/api/v1/games/1/moves", json={"x": 0, "y": 1})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Player O won")
        self.assertEqual(
            data["board"], [["X", "X", "O"], ["X", "O", "X"], ["O", "O", "O"]]
        )


if __name__ == "__main__":
    unittest.main()
