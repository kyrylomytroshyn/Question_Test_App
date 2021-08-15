from polls.models import Test
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework.filters import DateTimeFilter, CharFilter


class TestFilterSettings(FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')
    start_date = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    end_date = DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Test
        fields = ['title', 'created_at']