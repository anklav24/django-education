from django import forms

from django.core.exceptions import ValidationError
from .models import BookInstance
from django.forms import ModelForm
import datetime  # for checking renewal date range.


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')

        # Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data


class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Проверка того, что дата не в прошлом
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')

        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # Не забывайте всегда возвращать очищенные данные
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back',]
        labels = {'due_back': 'Renewal date', }
        help_texts = {'due_back': 'Enter a date between now and 4 weeks (default 3).', }
