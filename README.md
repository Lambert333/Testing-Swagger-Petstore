# 📋 Автотесты для Petstore API

Этот проект содержит автотесты для публичного API [Swagger Petstore](https://petstore.swagger.io/), реализованные на Python с использованием Pytest и Requests.

---

## 📦 Стек технологий

- **Python 3.13**
- **Pytest** — запуск тестов
- **Requests** — HTTP-запросы
- **pytest.ini** — конфигурация тестов
- **conftest.py** — фикстуры для переиспользования
- **utils/** — вспомогательные модули (payloads, генераторы данных и т.д.)

---

## Структура проекта

```
.
├── endpoints/              # Классы для работы с эндпоинтами API
│   ├── pet_endpoint.py    # Методы для работы с питомцами
│   ├── store_endpoint.py  # Методы для работы с заказами
│   └── user_endpoint.py   # Методы для работы с пользователями
├── tests/                 # Тесты
│   ├── resources/         # Ресурсы для тестов (изображения и т.д.)
│   ├── test_pet.py       # Тесты для питомцев
│   ├── test_store.py     # Тесты для заказов
│   └── test_user.py      # Тесты для пользователей
├── utils/                 # Вспомогательные классы и функции
│   ├── base_endpoint.py  # Базовый класс для работы с API
│   ├── data_generator.py # Генераторы тестовых данных
│   ├── oauth_handler.py  # Обработчик OAuth аутентификации
│   ├── retry.py          # Декоратор для повторных попыток
│   └── session_generator.py # Генератор сессий для запросов
├── API_BUGS.md           # Документация несоответствий API
├── conftest.py           # Фикстуры pytest
├── pytest.ini           # Конфигурация pytest
└── requirements.txt     # Зависимости проекта
```

## 🚀 Как запустить проект локально

1. Клонировать репозиторий:
    ```bash
    git clone https://github.com/Lambert333/Testing-Swagger-Petstore.git
    cd Testing-Swagger-Petstore
    ```

2. Создать и активировать виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # для Linux/Mac
    .\venv\Scripts\activate    # для Windows
    ```

3. Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустить тесты:
    ```bash
    pytest -v
    ```

---

## 🧑‍💻 Автор

[Дементьев Иван]