from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category, get_total_spent_amount, get_summary_per_year_month


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            date_from = form.cleaned_data.get('date_from', '')
            date_to = form.cleaned_data.get('date_to', '')
            category = form.cleaned_data.get('category', '')
            sorted_by = form.cleaned_data.get('sorted_by', '')
            ordering = form.cleaned_data.get('ordering', '')
            if name:
                queryset = queryset.filter(name__icontains=name)
            elif date_from and date_to:
                queryset = queryset.filter(date__range=[date_from, date_to])
            elif date_to:
                queryset = queryset.filter(date__lte=date_to)
            elif date_from:
                queryset = queryset.filter(date__gte=date_from)
            elif category:
                queryset = queryset.filter(category__in=category)
            elif sorted_by:
                queryset = queryset.order_by(ordering + sorted_by)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            total_spent_amount=get_total_spent_amount(queryset),
            total_spent_per_year_month=get_summary_per_year_month(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

