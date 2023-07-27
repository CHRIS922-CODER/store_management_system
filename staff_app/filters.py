import django_filters
from commodity_app.models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields =  ['name','category']

        