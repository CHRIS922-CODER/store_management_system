from django.urls import path
from . import views
urlpatterns = [
    path('',views.item_list, name="item_list"),
    path('index',views.index,name='index'),
    path('issuance_request/<int:product_id>/', views.issuance_request, name='issuance_request'),
    path('issuance_history',views.issuance_history, name='issuance_history'),
    path('issuance_editing/<int:id>',views.issuance_editing,name='issuance_editing')
]