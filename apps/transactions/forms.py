from django import forms
from .models.transaction import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'  # или укажи конкретные поля, если нужно

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            # Добавляем класс 'form-control', если его ещё нет
            classes = existing_classes + ' form-control' if 'form-control' not in existing_classes else existing_classes
            field.widget.attrs['class'] = classes.strip()
