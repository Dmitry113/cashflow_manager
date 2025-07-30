import pytest
from django.core.exceptions import ValidationError
from apps.transactions.forms import TransactionForm
from apps.transactions.models.directory import Status, Type, Category, SubCategory

@pytest.mark.django_db
def test_transaction_form_valid_and_invalid():
    # Создаем справочные объекты
    type_income = Type.objects.create(name="Доход")
    type_expense = Type.objects.create(name="Расход")

    status = Status.objects.create(name="Активный")

    category_income = Category.objects.create(name="Зарплата", type=type_income)
    category_expense = Category.objects.create(name="Продукты", type=type_expense)

    subcategory_income = SubCategory.objects.create(name="Основная зарплата", category=category_income)
    subcategory_expense = SubCategory.objects.create(name="Мясо", category=category_expense)

    # Валидные данные
    valid_data = {
        "status": status.id,
        "type": type_income.id,
        "category": category_income.id,
        "subcategory": subcategory_income.id,
        "amount": "1000.00",
        "comment": "Тестовый доход",
        "manual_date": "2025-07-30",
    }
    form = TransactionForm(data=valid_data)
    assert form.is_valid()

    # Невалидная форма — категория не принадлежит типу
    invalid_data_category = valid_data.copy()
    invalid_data_category["category"] = category_expense.id  # категория расхода для типа дохода
    form = TransactionForm(data=invalid_data_category)
    assert not form.is_valid()
    assert "Выбранная категория не принадлежит выбранному типу." in str(form.errors)

    # Невалидная форма — подкатегория не принадлежит категории
    invalid_data_subcategory = valid_data.copy()
    invalid_data_subcategory["subcategory"] = subcategory_expense.id  # подкатегория расхода для категории дохода
    form = TransactionForm(data=invalid_data_subcategory)
    assert not form.is_valid()
    assert "Выбранная подкатегория не принадлежит выбранной категории." in str(form.errors)
