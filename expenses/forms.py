from datetime import date

from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=False)
    date_to = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Expense
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
