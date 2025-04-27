class BaseEndpoint:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.response = None
        self.response_json = None

    def post(self, path: str, payload=None, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        self.response = self.session.post(url, json=payload, **kwargs)
        self._handle_response(expected_status)
        return self.response

    def get(self, path: str, params=None, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        self.response = self.session.get(url, params=params, **kwargs)
        self._handle_response(expected_status)
        return self.response

    def put(self, path: str, payload=None, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        self.response = self.session.put(url, json=payload, **kwargs)
        self._handle_response(expected_status)
        return self.response

    def delete(self, path: str, expected_status=200, **kwargs):
        url = f"{self.base_url}{path}"
        self.response = self.session.delete(url, **kwargs)
        self._handle_response(expected_status)
        return self.response

    def check_field_value(self, field, expected_value):
        assert self.response_json[field] == expected_value, (
            f"Expected {field} to be {expected_value}, got {self.response_json[field]}"
        )

    def _handle_response(self, expected_status):
        assert self.response.status_code == expected_status, (
            f"Expected status {expected_status}, got {self.response.status_code}"
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = None