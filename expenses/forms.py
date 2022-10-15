from django import forms

from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=False)
    date_to = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=False)
    category = forms.MultipleChoiceField(choices=[(category.id, category.name) for category in Category.objects.all()],
                                         widget=forms.CheckboxSelectMultiple, required=False)
    sorted_by = forms.ChoiceField(choices=[('category', 'category'),
                                           ('date', 'date')], widget=forms.RadioSelect, required=False)
    ordering = forms.ChoiceField(choices=[('', 'ascending'),
                                          ('-', 'descending')], widget=forms.RadioSelect, required=False)

    class Meta:
        model = Expense
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
