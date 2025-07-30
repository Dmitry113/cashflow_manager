from django.db import models


class Status(models.Model):
    name = models.CharField("Название статуса", max_length=50, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField("Название типа", max_length=50, unique=True)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name="Тип"
    )

    class Meta:
        unique_together = ('name', 'type')
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} ({self.type.name})"


class SubCategory(models.Model):
    name = models.CharField("Название подкатегории", max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name="Категория"
    )

    class Meta:
        unique_together = ('name', 'category')
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return f"{self.name} ({self.category.name})"
