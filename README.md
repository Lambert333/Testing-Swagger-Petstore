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

## 📁 Структура проекта

```bash
.
├── endpoints/    # Обёртки над API методами (по ресурсам Pet, Store, User)
├── tests/        # Тесты для Pet, Store и User
├── utils/        # Утилиты: генерация данных, заготовки запросов
├── conftest.py   # Общие фикстуры
├── pytest.ini    # Настройки Pytest
├── requirements.txt # Зависимости
├── README.md     # Документация проекта
└── .gitignore    # Исключения для Git
```

---

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
---

## 🧑‍💻 Автор

[Дементьев Иван]