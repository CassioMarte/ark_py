from flask import Blueprint, jsonify, Request

pets_routes_bp = Blueprint("pets_routes", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def get_list_pets():
    return {"olá": "Mundo"}