from src.views.http_types.http_request import HttpRequest
from src.main.composer.people_creator_composer import people_creator_compose
from src.main.composer.find_people_composer import find_people_composer
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

@people_routes_bp.route("/people/<person_uuid>", methods=["GET"])
def find_people():
    try:
        http_request = HttpRequest(param={ "person_uuid": person_uuid })

        view = find_people_composer()

        http_response = view.handle(http_request)

        return jsonify(http_request)
    except Exception as exception:
        return jsonify(http_response.body), http_response.status_code