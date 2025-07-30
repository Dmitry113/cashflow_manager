from django.db import models
from django.core.exceptions import ValidationError
from .directory import Status, Type, Category, SubCategory


class Transaction(models.Model):
    created_at = models.DateField("Дата создания", auto_now_add=True)
    manual_date = models.DateField("Дата вручную", null=True, blank=True)

    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.PROTECT)
    type = models.ForeignKey(Type, verbose_name="Тип", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, verbose_name="Подкатегория", on_delete=models.PROTECT)

    amount = models.DecimalField("Сумма", max_digits=12, decimal_places=2)
    comment = models.TextField("Комментарий", blank=True)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    def clean(self):
        if self.category.type != self.type:
            raise ValidationError("Выбранная категория не принадлежит выбранному типу.")
        if self.subcategory.category != self.category:
            raise ValidationError("Выбранная подкатегория не принадлежит выбранной категории.")

    def __str__(self):
        return f"{self.manual_date or self.created_at} | {self.amount} | {self.type.name}"
