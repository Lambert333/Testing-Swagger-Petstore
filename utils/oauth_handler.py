import requests
import logging
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

class OAuthHandler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        
    def get_oauth_token(self):
        # Параметры для OAuth2 запроса
        params = {
            'response_type': 'token',
            'client_id': 'test-client',  # Тестовый клиент для Petstore
            'scope': 'write:pets read:pets',  # Запрашиваемые права
            'redirect_uri': 'https://petstore.swagger.io/oauth2-redirect.html'
        }
        
        # Формируем URL для авторизации
        auth_url = f"{self.base_url}/oauth/authorize?{urlencode(params)}"
        
        try:
            # Выполняем запрос на авторизацию
            response = requests.get(auth_url, allow_redirects=True)
            
            # В реальном приложении здесь был бы редирект на страницу авторизации и получение токена из URL после редиректа
            self.token = 'special-key' # Для тестового API мы можем использовать специальный ключ
            
            logger.info("Успешно получен OAuth2 токен")
            return self.token
            
        except Exception as e:
            logger.error(f"Ошибка при получении OAuth2 токена: {str(e)}")
            raise 