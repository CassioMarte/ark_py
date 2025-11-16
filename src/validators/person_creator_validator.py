from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.erro_types.http_unprocessable_entity import HttpUnprocessableEntityError

def person_creator_validator(http_request: HttpRequest)-> None:

    class BodyData(BaseModel):
        first_name: constr(min_length=1) # type: ignore
        last_name: constr(min_length=1) # type: ignore
        age: int
        pet_id: constr(min_length=10) # type: ignore

    
    try:
        BodyData(**http_request.body) # ** para entrar em body e dividi-lo em first_name= xxxx, last_name=xxx, age: XX   pet_id: xxx

    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e