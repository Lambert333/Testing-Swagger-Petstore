import time
import pytest
from endpoints.pet_endpoint import PetEndpoint
from utils.data_generator import generate_valid_pet_payload, generate_minimal_valid_pet_payload


# создание питомца с валидными данными
def test_create_pet_with_valid_data(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = generate_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.check_field_value("name", payload["name"])
    pet.check_field_value("status", payload["status"])
    pet.get_pet_by_id(payload["id"], 200)  # проверяем, что питомец действительно создается


# создание питомца с минимальными валидными данными
def test_create_pet_with_minimal_valid_data(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = generate_minimal_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.check_field_value("id", payload["id"])
    pet.check_field_value("name", payload["name"])
    pet.get_pet_by_id(payload["id"], 200)  # проверяем, что питомец действительно создается


# создание питомца с payload={}
def test_create_pet_with_empty_payload(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = {}
    pet.add_pet(payload, 200)


# создание питомца с payload="null"
def test_create_pet_with_null_payload(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = "null"
    pet.add_pet(payload, 500)


# создание питомца с разными статусами
@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_create_pet_with_different_statuses(session, base_url, status):
    pet = PetEndpoint(session, base_url)
    payload = generate_valid_pet_payload()
    payload["status"] = status
    pet.add_pet(payload, 200)
    pet.check_field_value("status", status)
    response = pet.get_pet_by_id(payload["id"], 200).json()
    pet.check_field_value("status",
                          response["status"])  # проверяем, что питомец действительно создается с указанным статусом


# получения данных о созданном питомце
def test_get_pet(session, base_url):
    pet = PetEndpoint(session, base_url)
    payload = generate_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.get_pet_by_id(payload["id"], 200)


# получение данных о несуществующем питомце
def test_get_nonexistent_pet(session, base_url):
    pet = PetEndpoint(session, base_url)
    pet.get_pet_by_id("123321", 404)


# получение данных по id с неверным форматом
def test_get_pet_with_invalid_id(session, base_url):
    # Примечание: API возвращает 404 вместо 400, как указано в документации.
    pet = PetEndpoint(session, base_url)
    pet.get_pet_by_id("invalid id", 404)  # API возвращает 404 вместо 400


# получение списка питомцев по валидном статусу
@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_get_pets_by_status(session, status, base_url):
    pet = PetEndpoint(session, base_url)
    pet.get_pets_by_status(status, 200)


# получение списка питомцев по невалидному статусу
def test_get_pets_by_status_with_invalid_status(session, base_url, status="invalid_status"):
    # Примечание: API принимает любой статус вместо возврата 400.
    pet = PetEndpoint(session, base_url)
    pet.get_pets_by_status(status, 200)  # API возвращает 200 вместо 400


# обновление существующего питомца через форму
def test_update_pet(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = generate_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.update_pet_with_form(
        pet_id=payload["id"],
        name="Updated Name",
        status="sold",
        expected_status=200)
    response = pet.get_pet_by_id(payload["id"], 200).json()
    pet.check_field_value("name", response["name"])
    pet.check_field_value("status", response["status"])


# обновление несуществующего питомца
def test_update_nonexistent_pet(session, base_url):
    # Примечание: API создает нового питомца вместо возврата 404.
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = generate_valid_pet_payload()
    payload["id"] = time.time()  # несуществующий ID
    response = pet.update_pet(payload, 200).json()  # API создает нового питомца вместо возврата 404
    pet.get_pet_by_id(response["id"], 200)


# обновление питомца с неверным форматом данных
def test_update_pet_with_invalid_data(session, base_url):
    # Примечание: API принимает любые данные вместо возврата 405.
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = generate_valid_pet_payload()
    pet.add_pet(payload, 200)
    invalid_payload = payload.copy()
    invalid_payload["status"] = "invalid_status"  # неверный статус
    pet.update_pet(invalid_payload, 200)  # API принимает любые данные


# удаление питомца
def test_delete_pet(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = generate_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.get_pet_by_id(payload["id"], 200)
    pet.delete_pet(payload["id"], 200)
    pet.get_pet_by_id(payload["id"], 404)  # проверяем, что питомец действительно удаляется


# загрузка изображения для существующего питомца
def test_upload_pet_image(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    payload = generate_valid_pet_payload()
    pet.add_pet(payload, 200)
    pet.upload_pet_image(
        pet_id=payload["id"],
        file_path="tests/resources/test_image.jpg",
        additional_metadata="Test metadata",
        expected_status=200
    )
    pet.check_response_content(
        expected_code=200,
        required_fields=["message", "type"],
        message_contains=["File uploaded to", "Test metadata"])


# загрузка изображения для несуществующего питомца
def test_upload_pet_image_nonexistent_pet(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    # Примечание: API возвращает 200, но создает новый питомец
    pet.upload_pet_image(
        pet_id=999999999,
        file_path="tests/resources/test_image.jpg",
        expected_status=200
    )
    pet.check_response_content(
        expected_code=200,
        required_fields=["message", "type"],
        message_contains=["File uploaded to", "additionalMetadata: null"]
    )


# загрузка изображения с неверным форматом ID
def test_upload_pet_image_invalid_id(session, base_url):
    pet = PetEndpoint(session=session, base_url=base_url)
    # Примечание: API возвращает 404 с сообщением о NumberFormatException
    pet.upload_pet_image(
        pet_id="invalid_id",
        file_path="tests/resources/test_image.jpg",
        expected_status=404
    )
    pet.check_response_content(
        expected_code=404,
        required_fields=["message", "type"],
        message_contains=["NumberFormatException"]
    )
