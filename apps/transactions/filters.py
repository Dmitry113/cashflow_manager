import django_filters
from apps.transactions.models.transaction import Transaction


class TransactionFilter(django_filters.FilterSet):
    manual_date__gte = django_filters.DateFilter(field_name='manual_date', lookup_expr='gte')
    manual_date__lte = django_filters.DateFilter(field_name='manual_date', lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = ['status', 'type', 'category', 'subcategory', 'manual_date__gte', 'manual_date__lte']
