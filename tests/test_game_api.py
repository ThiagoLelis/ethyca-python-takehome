import unittest
from app import app

class TestGameApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_game(self):
        response = self.app.post("/api/v1/games")
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
        self.assertTrue(any("O" in row for row in board))

    def test_create_invalid_move(self):
        response = self.app.post("/api/v1/games")
        game_id = response.get_json()["game_id"]

        response = self.app.post(
            f"/api/v1/games/{game_id}/moves", json={"x": 1, "y": 1}
        )
        response = self.app.post(
            f"/api/v1/games/{game_id}/moves", json={"x": 1, "y": 1}
        )
        data = json.loads(response.get_json())

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
        self.assertEqual(data["message"], "Invalid move")

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

    def test_get_moves(self):
        response = self.app.post("/api/v1/games")
        game_id = response.get_json()["game_id"]
        self.app.post(f"/api/v1/games/{game_id}/moves", json={"x": 1, "y": 1})
        self.app.post(f"/api/v1/games/{game_id}/moves", json={"x": 2, "y": 2})
        self.app.post(f"/api/v1/games/{game_id}/moves", json={"x": 3, "y": 2})

        response = self.app.get(f"/api/v1/games/{game_id}/moves")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data["moves"]), 3)
        self.assertTrue(data["moves"][0]["game_id"] == game_id)
        self.assertTrue(data["moves"][0]["x"] == 1)
        self.assertTrue(data["moves"][0]["y"] == 1)
        self.assertTrue(data["moves"][1]["x"] == 2)
        self.assertTrue(data["moves"][1]["y"] == 2)
        self.assertTrue(data["moves"][2]["x"] == 3)
        self.assertTrue(data["moves"][2]["y"] == 2)


if __name__ == "__main__":
    unittest.main()
