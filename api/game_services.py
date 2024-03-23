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
    breakpoint()
    game_list = [{"game_id": game_id, "moves": len(games[game_id].moves), "winner": games[game_id].game_winner} for game_id in games]
    game_list.sort(key=lambda x: x['game_id'])
    return jsonify({"games": game_list})


def make_move(game_id, data):
    pass


def get_moves(game_id):
    pass
