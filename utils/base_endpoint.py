import logging
import time
from utils.retry import retry

logger = logging.getLogger(__name__)

class BaseEndpoint:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.response = None
        self.response_json = None


    # использование метода POST
    @retry(max_attempts=10, delay=1.0)
    def post(self, path: str, payload=None, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        # logger.info(f"POST request to {url}")
        # logger.info(f"Request headers: {self.session.headers}")
        # logger.info(f"Request cookies: {self.session.cookies.get_dict()}")
        self.response = self.session.post(url, json=payload, **kwargs)
        self._handle_response(expected_status)
        return self.response

    # использование метода GET
    @retry(max_attempts=10, delay=1.0)
    def get(self, path: str, params=None, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        # logger.info(f"GET request to {url}")
        # logger.info(f"Request headers: {self.session.headers}")
        # logger.info(f"Request cookies: {self.session.cookies.get_dict()}")
        self.response = self.session.get(url, params=params, **kwargs)
        self._handle_response(expected_status)
        return self.response

    # использование метода PUT
    @retry(max_attempts=10, delay=1.0)
    def put(self, path: str, payload=None, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        # logger.info(f"PUT request to {url}")
        # logger.info(f"Request headers: {self.session.headers}")
        # logger.info(f"Request cookies: {self.session.cookies.get_dict()}")
        self.response = self.session.put(url, json=payload, **kwargs)
        self._handle_response(expected_status)
        return self.response

    # использование метода DELETE
    @retry(max_attempts=10, delay=1.0)
    def delete(self, path: str, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        # logger.info(f"DELETE request to {url}")
        # logger.info(f"Request headers: {self.session.headers}")
        # logger.info(f"Request cookies: {self.session.cookies.get_dict()}")
        self.response = self.session.delete(url, **kwargs)
        self._handle_response(expected_status)
        return self.response

    # сравнение полей
    def check_field_value(self, field, expected_value):
        assert self.response_json[field] == expected_value, (
            f"Expected {field} to be {expected_value}, got {self.response_json[field]}")

    # Проверяет содержимое JSON-ответа
    def check_response_content(self, expected_code=None, required_fields=None, message_contains=None):
        """
            expected_code: ожидаемый код ответа
            required_fields: список обязательных полей в ответе
            message_contains: список строк, которые должны содержаться в сообщении
        """
        if expected_code is not None:
            assert self.response_json["code"] == expected_code, (
                f"Expected code {expected_code}, got {self.response_json['code']}"
            )
        
        if required_fields:
            for field in required_fields:
                assert field in self.response_json, f"Response should contain '{field}' field"
        
        if message_contains and "message" in self.response_json:
            for text in message_contains:
                assert text in self.response_json["message"], (
                    f"Response message should contain '{text}'"
                )

    def _handle_response(self, expected_status):
        # logger.info(f"Response status: {self.response.status_code}")
        # logger.info(f"Response headers: {self.response.headers}")
        # logger.info(f"Response cookies: {self.response.cookies.get_dict()}")
        assert self.response.status_code == expected_status, (
            f"Expected status {expected_status}, got {self.response.status_code}"
        )
        try:
            self.response_json = self.response.json()
            # logger.info(f"Response body: {self.response_json}")
        except ValueError:
            self.response_json = None