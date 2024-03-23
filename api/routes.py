from flask import Blueprint, jsonify, request

game_blueprint = Blueprint("game", __name__, url_prefix="/api/v1")


@game_blueprint.route("/games", methods=["POST"])
def new_game_route():
    return create_game()


@game_blueprint.route("/games/<string:game_id>/moves", methods=["POST"])
def make_move_route(game_id):
    data = request.get_json()
    return make_move(game_id, data)


@game_blueprint.route("/games/<string:game_id>/moves", methods=["GET"])
def get_moves_route(game_id):
    return get_moves(game_id)


@game_blueprint.route("/games/<string:game_id>", methods=["GET"])
def get_games_route(game_id):
    return get_games(game_id)
