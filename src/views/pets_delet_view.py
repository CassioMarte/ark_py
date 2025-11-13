from .interface.view_interface import ViewInterface
from src.controllers.interfaces.pets_delet_controller_interface import PetDeletControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class PetsDeleteView(ViewInterface):
    def __init__(self, pets_delete_controller: PetDeletControllerInterface)-> None:
        self.__pets_delete_controller = pets_delete_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pet_uuid = http_request.param["pet_uuid"]
        self.__pets_delete_controller.delet_pet(pet_uuid)

        return HttpResponse(status_code=204)