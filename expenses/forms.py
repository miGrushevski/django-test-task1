from datetime import date

from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=False)
    date_to = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=False)
    category = forms.MultipleChoiceField(choices=[(category.id, category.name) for category in Category.objects.all()],
                                         widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Expense
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
