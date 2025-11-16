from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body)->None:
        self.body = body
    
def test_person_create_validator():
    request = MockRequest({
        "first_name": "Teste",
        "last_name": "Validator",
        "age": 30,
        "pet_id": "85w5w2s1c1582w12d62"
    })

    person_creator_validator(request)  # type: ignore