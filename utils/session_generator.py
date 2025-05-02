import random
import string


def generate_session_id():
    # Генерирует JSESSIONID в формате: 32 символа (буквы и цифры)
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=32))


def generate_user_id():
    # Генерирует userId в формате: 20 цифр
    return str(random.randint(10000000000000000000, 99999999999999999999))
