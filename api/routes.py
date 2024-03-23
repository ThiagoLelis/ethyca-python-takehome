from flask import Blueprint, jsonify, request

from api.game_services import create_game, make_move, get_moves, get_games

game_blueprint = Blueprint("game", __name__, url_prefix="/api/v1")


@game_blueprint.route("/games", methods=["POST"])
def new_game_route():
    return create_game()


@game_blueprint.route("/games", methods=["GET"])
def get_games_route():
    return get_games()


@game_blueprint.route("/games/<string:game_id>/moves", methods=["POST"])
def make_move_route(game_id):
    data = request.get_json()
    return make_move(int(game_id), data)


@game_blueprint.route("/games/<string:game_id>/moves", methods=["GET"])
def get_moves_route(game_id):
    return get_moves(int(game_id))
