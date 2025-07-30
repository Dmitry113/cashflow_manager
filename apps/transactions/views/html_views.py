from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from apps.transactions.models.transaction import Transaction
from apps.transactions.forms import TransactionForm

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10  # если хочешь пагинацию

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction-list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction-list')
