
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('add_product',views.add_product,name="add_product"),
    path('product_list',views.product_list,name="product_list"),
    path('export_productList_to_csv',views.export_productList_to_csv, name="export_departmentList_to_csv"),
    path('product_edit/<int:id>/',views.product_edit,name="product_edit"),
    path('product_delete/<int:id>/',views.product_delete,name="product_delete"),
    path('reorder_level/<int:id>',views.reorder_level,name='reorder_level'),
    path('product_reorder_level_list',views.product_reorder_level_list,name="product_reorder_level_list"),
    path('export_to_pdf_product',views.export_to_pdf_product,name="export_to_pdf_product"),
    path('export_to_pdf_product_out_of_stock',views.export_to_pdf_product_out_of_stock,name="export_to_pdf_product_out_of_stock"),

    path('product_name',views.product_name,name='product_name'),
    path('product_name_edit/<int:id>/',views.product_name_edit,name="product_name_edit"),
    path('product_name_delete/<int:id>/',views.product_name_delete,name="product_name_delete"),
    path('product_name_list',views.product_name_list,name='product_name_list'),

    path('add_category',views.add_category,name="add_category"),
    path('category_list',views.category_list,name="category_list"),
    path('export_categoryList_to_csv',views.export_categoryList_to_csv, name="export_categoryList_to_csv"),
    path('category_edit/<int:id>/',views.category_edit,name="category_edit"),
    path('category_delete/<int:id>/',views.category_delete,name="category_delete"),

    path('add_department',views.add_department,name="add_department"),
    path('department_list',views.department_list,name="department_list"),
    path('export_departmentList_to_csv',views.export_departmentList_to_csv, name="export_departmentList_to_csv"),
    path('department_edit/<int:id>/',views.department_edit,name="department_edit"),
    path('department_delete/<int:id>/',views.department_delete,name="department_delete"),

    path('add_issuance/<int:product_id>/',views.add_issuance,name="add_issuance"),
    path('issuance_list',views.issuance_list,name="issuance_list"),
    path('export_issuanceList_to_csv/', views.export_to_csv, name='export_to_csv'),
    path('issuance_edit/<int:id>/',views.issuance_edit,name="issuance_edit"),
    path('issuance_delete/<int:id>/',views.issuance_delete,name="issuance_delete"),
    path('issuance_records',views.issuance_records,name="issuance_records"),
    path('export_issuanceRecords_to_csv/', views.export_issuanceRecords_to_csv, name='export_issuanceRecords_to_csv'),
    path('export_to_pdf_issuance',views.export_to_pdf_issuance,name="export_to_pdf_issuance"),


    path('export_to_csv/', views.export_to_csv, name='export_to_csv'),
    path('settings',views.settings,name='settings')
]
