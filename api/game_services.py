import uuid
from flask import jsonify

from api.game_logic import TicTacToeGame

# This is the dictionary that will perform the function of a database
# Using a database is recommended
# However, due to the short implementation time, I decided to store the games in memory
games = {}


def create_game(size=3):
    game_id = len(games) + 1
    games[game_id] = TicTacToeGame(size=size)
    return jsonify({"game_id": game_id, "message": "Game created successfully"}), 201


def get_games():
    game_list = [
        {
            "game_id": game_id,
            "moves": len(games[game_id].moves),
            "winner": games[game_id].game_winner,
        }
        for game_id in games
    ]
    game_list.sort(key=lambda x: x["game_id"])
    return jsonify({"games": game_list})


def make_move(game_id, data):
    if game_id not in games:
        return jsonify({"message": "Game not found"}), 404

    game = games[game_id]
    x, y = data.get("x"), data.get("y")

    if x is None or y is None:
        return jsonify({"message": "Invalid coordinates"}), 400

    if not (0 <= x <= game.size -1 and 0 <= y <= game.size - 1):
        return jsonify({"message": "Coordinates out of bounds"}), 400

    if game.make_move(x, y):
        is_winner, winner = game.check_winner()
        if is_winner:
            game.game_winner = winner
            return jsonify({"message": f"Player {winner} won", "board": game.board}), 200
        
        game.random_move()
        is_winner, winner = game.check_winner()
        if is_winner:
            game.game_winner = winner
            return jsonify({"message": f"Player {winner} won", "board": game.board}), 200
        
        return jsonify({"message": "Move created successfully", "board": game.board}), 201

    else:
        return jsonify({"message": "Invalid move"}), 400


def get_moves(game_id):
    if game_id not in games:
        return jsonify({"message": "Game not found"}), 404

    game = games[game_id]
    game.moves.sort(key=lambda x: x["id"])
    return jsonify({"game_id": game_id, "moves": game.moves, "board": game.board})
