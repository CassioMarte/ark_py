from flask import Blueprint, jsonify
from src.main.composer.pets_lister_composer import pets_lister_composer
from src.main.composer.pets_delet_composer import pets_delet_composer
from src.views.http_types.http_request import HttpRequest
pets_routes_bp = Blueprint("pets_routes", __name__)
from src.errors.handle_errors import handle_errors

@pets_routes_bp.route("/pets", methods=["GET"])
def pets_lister():
    try:
        http_request = HttpRequest()

        view = pets_lister_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response)
      
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@pets_routes_bp.route("/pets_delet/<pet_uuid>", methods=["DELETE"])
def delet_pet(pet_uuid):
    try:
        http_request = HttpRequest(param={"pet_uuid": pet_uuid})

        view = pets_delet_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code