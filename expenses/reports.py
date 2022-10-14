from collections import OrderedDict
from datetime import datetime

from django.db.models import Sum, Value
from django.db.models.functions import Coalesce, ExtractYear, ExtractMonth


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def get_total_spent_amount(queryset):
    return queryset.aggregate(Sum('amount'))['amount__sum']


def get_summary_per_year_month(queryset):
    years_months = OrderedDict()
    years = sorted(set(x['year'] for x in queryset.annotate(year=ExtractYear('date')).values('year')))
    for year in years:
        months = sorted(set(x['month'] for x in queryset
                            .filter(date__year=year)
                            .annotate(month=ExtractMonth('date'))
                            .values('month')))
        for month in months:
            spent_per_month = \
                queryset.filter(date__year=year, date__month=month).aggregate(Sum('amount'))['amount__sum']
            datetime_object = datetime.strptime(str(month), "%m")
            month_name = datetime_object.strftime("%b")
            years_months[f'{year}-{month_name}'] = spent_per_month
    return years_months
