import pytest
from endpoints.pet_endpoint import PetEndpoint
from utils.data_generator import generate_valid_pet_payload, generate_invalid_pet_payload, \
    generate_minimal_valid_pet_payload


def test_create_pet_with_valid_data(session, base_url):
    pet=PetEndpoint(session=session, base_url=base_url)
    payload = generate_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.check_field_value("name", payload["name"])
    pet.check_field_value("status", payload["status"])

def test_create_pet_with_minimal_invalid_data(session, base_url):
    pet=PetEndpoint(session=session, base_url=base_url)
    payload =generate_minimal_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.check_field_value("id", payload["id"])
    pet.check_field_value("name", payload["name"])

def test_create_pet_with_empty_payload(session, base_url):
    pet=PetEndpoint(session=session, base_url=base_url)
    payload={}
    pet.add_pet(payload, 405)

@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_create_pet_with_different_statuses(session, base_url, status):
    pet = PetEndpoint(session, base_url)
    payload = generate_valid_pet_payload()
    payload["status"] = status
    pet.add_pet(payload,200)
    pet.check_field_value("status", status)