from rest_framework import serializers
from .models.transaction import Transaction
from .models.directory import Status, Type, Category, SubCategory


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField(read_only=True)  # выводим type.name

    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)  # выводим category.name

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']

class TransactionSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField(read_only=True)
    type = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    subcategory = serializers.StringRelatedField(read_only=True)

    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source='status', write_only=True
    )
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), source='type', write_only=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(), source='subcategory', write_only=True
    )

    class Meta:
        model = Transaction
        fields = [
            'id',
            'created_at',
            'manual_date',
            'status', 'status_id',
            'type', 'type_id',
            'category', 'category_id',
            'subcategory', 'subcategory_id',
            'amount',
            'comment',
        ]

    def validate(self, data):
        # Берём объекты для проверки логики
        type_obj = data.get('type') or self.instance.type if self.instance else None
        category_obj = data.get('category') or self.instance.category if self.instance else None
        subcategory_obj = data.get('subcategory') or self.instance.subcategory if self.instance else None

        if category_obj and type_obj and category_obj.type != type_obj:
            raise serializers.ValidationError("Выбранная категория не принадлежит выбранному типу.")

        if subcategory_obj and category_obj and subcategory_obj.category != category_obj:
            raise serializers.ValidationError("Выбранная подкатегория не принадлежит выбранной категории.")

        return data
