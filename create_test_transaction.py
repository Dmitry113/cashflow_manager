from apps.transactions.models import Transaction, Status, Type, Category, SubCategory
from datetime import date

def create_test_transaction():
    status = Status.objects.first()
    type_ = Type.objects.first()
    if not type_:
        print("❌ Не найден ни один Type. Добавь хотя бы одну запись в модель Type.")
        return

    category = Category.objects.filter(type=type_).first()
    if not category:
        print(f"❌ Не найдена Category для Type: {type_}. Добавь хотя бы одну Category связанную с ним.")
        return

    subcategory = SubCategory.objects.filter(category=category).first()
    if not subcategory:
        print(f"❌ Не найдена SubCategory для Category: {category}. Добавь хотя бы одну SubCategory связанную с ней.")
        return

    transaction = Transaction.objects.create(
        manual_date=date.today(),
        status=status,
        type=type_,
        category=category,
        subcategory=subcategory,
        amount=1000,
        comment="Оплата налога за апрель"
    )
    print(f"✅ Транзакция создана: {transaction}")
