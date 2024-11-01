# Проект

## Установка и запуск
1. Склонируйте репозиторий:
   ```bash
   git clone git@github.com:Mir1a/test_proiject_for_ASAP_DEMO.git
   cd test_proiject_for_ASAP_DEMO

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv

3. Активируйте виртуальное окружение

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt

5. Создайте PostgreSQL сервер для тестирования.

6. Создайте файл .env в корневой директории проекта по примеру:
    ```bash
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASS=postgres

7. Проведите миграции:
   ```bash
   python manage.py migrate

8. Запустите проект:
   ```bash
   python manage.py runserver

9. Проверьте эндпоинты: Откройте http://127.0.0.1:8000/api/swagger/ в вашем браузере.

10. Для запуска тестов используйте:
    ```bash
    python manage.py test