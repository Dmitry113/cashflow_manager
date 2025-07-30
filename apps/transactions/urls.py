from django.urls import path

from apps.transactions.views.delete import TransactionDeleteView
from apps.transactions.views.html_views import TransactionListView, TransactionCreateView, TransactionUpdateView

app_name = 'transactions'

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction-list'),               # /transactions/
    path('create/', TransactionCreateView.as_view(), name='transaction-create'),    # /transactions/create/
    path('edit/<int:pk>/', TransactionUpdateView.as_view(), name='transaction-edit'),  # /transactions/edit/1/
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),  # /transactions/1/delete/
]
