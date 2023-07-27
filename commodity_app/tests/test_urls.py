from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .. import views

class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)
    
    def test_add_product_url(self):
        url = reverse('add_product')
        self.assertEqual(resolve(url).func, views.add_product)

    def test_product_list_url(self):
        url = reverse('product_list')
        self.assertEqual(resolve(url).func, views.product_list)

    def test_export_productList_to_csv_url(self):
        url = reverse('export_departmentList_to_csv')
        self.assertEqual(resolve(url).func, views.export_productList_to_csv)

    def test_product_edit_url(self):
        url = reverse('product_edit', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.product_edit)

    def test_product_delete_url(self):
        url = reverse('product_delete', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.product_delete)

    def test_reorder_level_url(self):
        url = reverse('reorder_level', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.reorder_level)

    def test_product_reorder_level_list_url(self):
        url = reverse('product_reorder_level_list')
        self.assertEqual(resolve(url).func, views.product_reorder_level_list)

    def test_export_to_pdf_product_url(self):
        url = reverse('export_to_pdf_product')
        self.assertEqual(resolve(url).func, views.export_to_pdf_product)

    def test_export_to_pdf_product_out_of_stock_url(self):
        url = reverse('export_to_pdf_product_out_of_stock')
        self.assertEqual(resolve(url).func, views.export_to_pdf_product_out_of_stock)

    # Add more test methods for the remaining URLs

# ... previous test methods ...

    def test_product_name_url(self):
        url = reverse('product_name')
        self.assertEqual(resolve(url).func, views.product_name)

    def test_product_name_edit_url(self):
        url = reverse('product_name_edit', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.product_name_edit)

    def test_product_name_delete_url(self):
        url = reverse('product_name_delete', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.product_name_delete)

    def test_product_name_list_url(self):
        url = reverse('product_name_list')
        self.assertEqual(resolve(url).func, views.product_name_list)

    def test_add_category_url(self):
        url = reverse('add_category')
        self.assertEqual(resolve(url).func, views.add_category)

    def test_category_list_url(self):
        url = reverse('category_list')
        self.assertEqual(resolve(url).func, views.category_list)

    def test_export_categoryList_to_csv_url(self):
        url = reverse('export_categoryList_to_csv')
        self.assertEqual(resolve(url).func, views.export_categoryList_to_csv)

    def test_category_edit_url(self):
        url = reverse('category_edit', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.category_edit)

    def test_category_delete_url(self):
        url = reverse('category_delete', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.category_delete)

    def test_add_department_url(self):
        url = reverse('add_department')
        self.assertEqual(resolve(url).func, views.add_department)

    def test_department_list_url(self):
        url = reverse('department_list')
        self.assertEqual(resolve(url).func, views.department_list)

    def test_export_departmentList_to_csv_url(self):
        url = reverse('export_departmentList_to_csv')
        self.assertEqual(resolve(url).func, views.export_departmentList_to_csv)

    def test_department_edit_url(self):
        url = reverse('department_edit', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.department_edit)

    def test_department_delete_url(self):
        url = reverse('department_delete', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.department_delete)

    def test_add_issuance_url(self):
        url = reverse('add_issuance', args=[1])  # Replace 1 with an appropriate product_id
        self.assertEqual(resolve(url).func, views.add_issuance)

    def test_issuance_list_url(self):
        url = reverse('issuance_list')
        self.assertEqual(resolve(url).func, views.issuance_list)

    def test_export_issuanceList_to_csv_url(self):
        url = reverse('export_to_csv')
        self.assertEqual(resolve(url).func, views.export_to_csv)

    def test_issuance_edit_url(self):
        url = reverse('issuance_edit', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.issuance_edit)

    def test_issuance_delete_url(self):
        url = reverse('issuance_delete', args=[1])  # Replace 1 with an appropriate ID
        self.assertEqual(resolve(url).func, views.issuance_delete)

    def test_issuance_records_url(self):
        url = reverse('issuance_records')
        self.assertEqual(resolve(url).func, views.issuance_records)

    def test_export_issuanceRecords_to_csv_url(self):
        url = reverse('export_issuanceRecords_to_csv')
        self.assertEqual(resolve(url).func, views.export_issuanceRecords_to_csv)

    def test_export_to_pdf_issuance_url(self):
        url = reverse('export_to_pdf_issuance')
        self.assertEqual(resolve(url).func, views.export_to_pdf_issuance)

    def test_export_to_csv_url(self):
        url = reverse('export_to_csv')
        self.assertEqual(resolve(url).func, views.export_to_csv)

    def test_settings_url(self):
        url = reverse('settings')
        self.assertEqual(resolve(url).func, views.settings)

# ... end of test methods ...
