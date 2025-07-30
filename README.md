# Cashflow Manager 💸

Веб-приложение для управления движением денежных средств. Поддерживает создание, редактирование, удаление и фильтрацию транзакций, работу со справочниками (статусы, типы, категории и подкатегории), а также веб-интерфейс и REST API.

## 🚀 Возможности

- CRUD-операции для транзакций
- Веб-интерфейс на Bootstrap 5
- Справочники: Тип, Статус, Категория, Подкатегория
- REST API с фильтрацией
- AJAX-загрузка подкатегорий

---

## ⚙️ Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/cashflow_manager.git
cd cashflow_manager

2. Создай и активируй виртуальное окружение

python -m venv .venv
source .venv/bin/activate        # Для Linux/Mac
.venv\Scripts\activate           # Для Windows

3. Установи зависимости

pip install -r requirements.txt

4. Создай .env файл

# .env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3

5. Примените миграции и создайте суперпользователя

python manage.py migrate
python manage.py createsuperuser

6. Запусти сервер

python manage.py runserver

🧪 Тесты

pytest

Или стандартно через Django:

python manage.py test

🖥️ Страницы
Главная: http://127.0.0.1:8000/

Транзакции (веб): http://127.0.0.1:8000/transactions/

API (список транзакций): http://127.0.0.1:8000/api/transactions/

🗃️ Структура проекта

cashflow_manager/
│
├── apps/
│   ├── transactions/         # Приложение транзакций
│   │   ├── models/           # Модели
│   │   ├── views/            # Представления
│   │   ├── forms.py          # Формы
│   │   ├── serializers.py    # Сериализаторы DRF
│   │   ├── urls.py           # Маршруты
│   │   └── templates/        # HTML-шаблоны
│
├── config/                   # Настройки Django
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── .env                      # Переменные окружения

📦 Зависимости
Python 3.10+

Django 5.2+

Django REST Framework

python-decouple

dj-database-url

Bootstrap 5 (CDN)

Разработал: Дмитрий Крупин