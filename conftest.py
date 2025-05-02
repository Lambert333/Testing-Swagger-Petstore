import pytest
import requests
import logging
from utils.session_generator import generate_session_id, generate_user_id
from utils.oauth_handler import OAuthHandler

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def base_url():
    return "https://petstore.swagger.io/v2"

# Фикстура для получения OAuth2 токена
@pytest.fixture(scope="session")
def oauth_token(base_url):
    oauth = OAuthHandler(base_url)
    return oauth.get_oauth_token()

# Фикстура для создания сессии с OAuth2 аутентификацией
@pytest.fixture(scope="session")
def session(base_url, oauth_token):
    with requests.Session() as session:
        # Устанавливаем динамически сгенерированные куки
        session.cookies.set('JSESSIONID', generate_session_id())
        session.cookies.set('userId', generate_user_id())
        
        # Устанавливаем заголовки для аутентификации
        session.headers.update({
            'api_key': oauth_token,
            'Authorization': f'Bearer {oauth_token}',
            'Content-Type': 'application/json'
        })
        
        logger.info("Создана сессия с OAuth2 аутентификацией")
        yield session
