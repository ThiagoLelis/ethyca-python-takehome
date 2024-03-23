from flask import Blueprint, jsonify, request

game_blueprint = Blueprint("game", __name__, url_prefix='/api/v1')