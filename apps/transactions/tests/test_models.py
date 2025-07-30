import pytest
from datetime import date
from apps.transactions.models.transaction import Transaction
from apps.transactions.models.directory import Status, Type, Category, SubCategory


@pytest.mark.django_db
def test_create_transaction():
    type_income = Type.objects.create(name="Доход")
    category = Category.objects.create(name="Зарплата", type=type_income)
    subcategory = SubCategory.objects.create(name="Основная работа", category=category)
    status = Status.objects.create(name="Завершено")

    transaction = Transaction.objects.create(
        amount=10000.00,
        manual_date=date.today(),      # заменено с date на manual_date
        comment="Зарплата за июль",   # заменено с description на comment
        type=type_income,
        status=status,
        category=category,
        subcategory=subcategory,
    )

    assert transaction.amount == 10000.00
    assert transaction.manual_date == date.today()
    assert transaction.comment == "Зарплата за июль"
    assert transaction.type == type_income
    assert transaction.status == status
    assert transaction.category == category
    assert transaction.subcategory == subcategory
