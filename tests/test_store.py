import time
from endpoints.store_endpoint import StoreEndpoint
from utils.data_generator import generate_valid_store_order_payload, generate_invalid_store_order_payload


# создание заказа с валидными данными
def test_add_order_with_valid_payload(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    payload = generate_valid_store_order_payload()
    store.add_order(payload, 200)
    store.check_field_value("id", payload["id"])
    store.get_order_by_id(payload["id"], 200)


# создание заказа с минимальным набором полей
def test_add_order_with_minimal_payload(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    payload = {
        "id": int(time.time()),
        "petId": 1,
        "quantity": 1
    }
    store.add_order(payload, 200)
    store.check_field_value("id", payload["id"])
    store.get_order_by_id(payload["id"], 200)


# создание заказа с пустым телом запроса
def test_add_order_with_empty_payload(session, base_url):
    # Примечание: API возвращает 200 OK вместо 400 Bad Request при пустом payload
    store = StoreEndpoint(session=session, base_url=base_url)
    store.add_order({}, 200)


# создание заказа с невалидными данными
def test_add_order_with_invalid_payload(session, base_url):
    # Примечание: API возвращает 500 вместо 400 при невалидных данных
    store = StoreEndpoint(session=session, base_url=base_url)
    payload = generate_invalid_store_order_payload()
    store.add_order(payload, 500)


# получение заказа по ID
def test_get_order_by_id(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    payload = generate_valid_store_order_payload()
    store.add_order(payload, 200)
    store.get_order_by_id(payload["id"], 200)


# получение несуществующего заказа
def test_get_nonexistent_order(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    store.get_order_by_id(999999, 404)


# получение заказа с неверным форматом ID
def test_get_order_with_invalid_id(session, base_url):
    # Примечание: API возвращает 404 вместо 400 при неверном формате ID
    store = StoreEndpoint(session=session, base_url=base_url)
    store.get_order_by_id("invalid_id", 404)


# получение статистики склада
def test_get_inventory_statistics(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    response = store.get_inventory_statistics(200)
    inventory = response.json()
    store.check_inventory_structure(inventory)


# удаление заказа
def test_delete_order(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    payload = generate_valid_store_order_payload()
    store.add_order(payload, 200)
    store.get_order_by_id(payload["id"], 200)
    store.delete_order(payload["id"], 200)
    store.get_order_by_id(payload["id"], 404)  # проверяем, что заказ действительно удален


# повторное удаление заказа
def test_delete_order_twice(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    payload = generate_valid_store_order_payload()
    store.add_order(payload, 200)
    store.delete_order(payload["id"], 200)
    store.delete_order(payload["id"], 404)  # при повторном удалении получаем 404


# удаление несуществующего заказа
def test_delete_nonexistent_order(session, base_url):
    store = StoreEndpoint(session=session, base_url=base_url)
    store.delete_order(999999, 404)


# удаление заказа с неверным форматом ID
def test_delete_order_with_invalid_id(session, base_url):
    # Примечание: API возвращает 404 вместо 400 при неверном формате ID
    store = StoreEndpoint(session=session, base_url=base_url)
    store.delete_order("invalid_id", 404)
