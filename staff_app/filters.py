import django_filters
from commodity_app.models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains',label='Product Name')
    class Meta:
        model = Product
        fields =  ['name','category']

        