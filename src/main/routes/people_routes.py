from src.views.http_types.http_request import HttpRequest
from src.main.composer.people_creator_composer import people_creator_compose
from flask import Blueprint, jsonify, request


people_routes_bp = Blueprint("people_routes", __name__)

@people_routes_bp.route("/people", methods=["POST"])
def create_people():
    try:
        http_request = HttpRequest(body=request.json)

        view = people_creator_compose()

        http_response = view.handle(http_request)

        return jsonify(http_request)
        
    except Exception as exception:
       # http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code