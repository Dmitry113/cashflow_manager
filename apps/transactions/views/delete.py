from django.urls import reverse_lazy
from django.views.generic import DeleteView
from apps.transactions.models import Transaction


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:transaction-list')
