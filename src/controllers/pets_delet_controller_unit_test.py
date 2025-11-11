from .pets_delet_controller import PetDeletController

def test_delet_pet_controller(mocker):
    mock_repository = mocker.Mock()

    controller = PetDeletController( mock_repository)

    controller.delet_pet("valid_uuid")

    # Como não tem retorno só verificamos se o método do repositório foi chamado corretamente
    mock_repository.delete_pet.assert_called_once_with("valid_uuid")