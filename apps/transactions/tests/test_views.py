import pytest
from django.urls import reverse
from apps.transactions.models import Type, Status, Category, SubCategory, Transaction

@pytest.mark.django_db
def test_transaction_create_view_get(client):
    url = reverse('transactions:transaction-create')  # <- исправлено имя
    response = client.get(url)
    assert response.status_code == 200
    assert b'<form' in response.content

@pytest.mark.django_db
def test_transaction_create_view_post_valid(client):
    type_income = Type.objects.create(name="Доход")
    status = Status.objects.create(name="Активный")
    category = Category.objects.create(name="Зарплата", type=type_income)
    subcategory = SubCategory.objects.create(name="Основная зарплата", category=category)

    url = reverse('transactions:transaction-create')  # <- исправлено имя
    data = {
        'date': '2024-07-30',
        'amount': 10000,
        'description': 'Тестовая транзакция',
        'type': type_income.id,
        'status': status.id,
        'category': category.id,
        'subcategory': subcategory.id,
    }

    response = client.post(url, data)
    assert response.status_code == 302  # Ожидается редирект после успешного создания
    assert Transaction.objects.count() == 1
