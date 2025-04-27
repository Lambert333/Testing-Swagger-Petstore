import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def session():
    with requests.Session() as session:
        yield session
