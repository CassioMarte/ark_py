from flask import Blueprint, jsonify, Request

health_routes_bp = Blueprint("health_routes", __name__)

@health_routes_bp.route("/health", methods=["GET"])
def get_list_pets():
    return "Route health, ok!"