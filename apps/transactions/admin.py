from django.contrib import admin
from .models.transaction import Transaction
from .models.directory import Status, Type, Category, SubCategory
from .forms import TransactionForm  # ← импорт кастомной формы


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    form = TransactionForm  # ← подключаем форму

    list_display = (
        "id",
        "formatted_date",
        "amount",
        "type",
        "status",
        "category",
        "subcategory",
        "short_comment",
    )
    list_filter = ("type", "status", "category", "subcategory")
    search_fields = ("comment",)
    date_hierarchy = "manual_date"

    def formatted_date(self, obj):
        return obj.manual_date or obj.created_at
    formatted_date.short_description = "Дата"

    def short_comment(self, obj):
        return (obj.comment[:50] + "...") if obj.comment and len(obj.comment) > 50 else obj.comment
    short_comment.short_description = "Комментарий"

    class Media:
        js = ('transactions/js/transaction_admin.js',)  # Подключаем свой JS


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    verbose_name = "Статус"
    verbose_name_plural = "Статусы"


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    verbose_name = "Тип"
    verbose_name_plural = "Типы"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    list_filter = ("type",)
    search_fields = ("name",)
    verbose_name = "Категория"
    verbose_name_plural = "Категории"


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)
    verbose_name = "Подкатегория"
    verbose_name_plural = "Подкатегории"
