import random
import string

def generate_valid_pet_payload(name=None, status="available"):
    payload = {
        "id": random.randint(100000, 999999),
        "category": {
            "id": random.randint(1, 100),
            "name": random.choice(["dog", "cat", "bird"])
        },
        "name": name or ''.join(random.choices(string.ascii_letters, k=8)),
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [
            {
                "id": random.randint(1, 100),
                "name": random.choice(["cute", "fluffy", "tiny"])
            }
        ],
        "status": status
    }
    return payload

def generate_minimal_valid_pet_payload(name=None, status="available"):
    payload = {
        "id": random.randint(100000, 999999),
        "name": name or ''.join(random.choices(string.ascii_letters, k=8)),
    }
    return payload

def generate_invalid_pet_payload():
    payload = {
        "id": "invalid_id",  # строка вместо числа
        "photoUrls": "should-be-a-list",  # ошибка типа
        "status": 12345  # неверный тип статуса
    }
    return payload

def generate_valid_store_order_payload():
    payload = {
        "id": random.randint(100000, 999999),
        "petId": random.randint(1000, 9999),
        "quantity": random.randint(1, 10),
        "shipDate": "2025-04-30T14:00:00.000Z",
        "status": random.choice(["placed", "approved", "delivered"]),
        "complete": random.choice([True, False])
    }
    return payload

def generate_invalid_store_order_payload():
    payload = {
        "id": "order_id",
        "petId": "not_a_pet_id",
        "quantity": "lots",
        "shipDate": "not-a-date",
        "status": "flying",  # неправильное значение статуса
        "complete": "yes"  # должно быть True/False
    }
    return payload

def generate_valid_user_payload():
    payload = {
        "id": random.randint(100000, 999999),
        "username": ''.join(random.choices(string.ascii_letters, k=8)),
        "firstName": random.choice(["John", "Jane", "Alice", "Bob"]),
        "lastName": random.choice(["Smith", "Doe", "Brown"]),
        "email": f"user{random.randint(1000,9999)}@example.com",
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "phone": f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}",
        "userStatus": random.randint(0, 1)
    }
    return payload

def generate_invalid_user_payload():
    payload = {
        "id": "user_id_string",
        "username": 12345,  # число вместо строки
        "firstName": None,
        "lastName": True,
        "email": "invalid-email-format",
        "password": 12345678,  # не строка
        "phone": ["123-456-7890"],  # список вместо строки
        "userStatus": "active"  # строка вместо числа
    }
    return payload
