from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.transactions.models.transaction import Transaction
from apps.transactions.serializers import TransactionSerializer
from apps.transactions.filters import TransactionFilter
from rest_framework.filters import SearchFilter


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-created_at')
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, SearchFilter]
    filterset_class = TransactionFilter  # Уже используется
    ordering_fields = ['manual_date', 'created_at', 'amount']
    ordering = ['-manual_date']
    search_fields = ['comment']  # <- вот здесь поиск по подстроке в комментарии

