from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product, Category, Department, Issuance
from ..forms import ProductForm, ProductNameForm, CategoryForm, DepartmentForm, IssuanceForm
from django.contrib.auth.models import User

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'commodity_app/mytemplate.html')

    def test_add_product_view(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_add.html')

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_list.html')

    def test_product_edit_view(self):
        product = Product.objects.create(name='Test Product', quantity=10)
        response = self.client.get(reverse('product_edit', args=[product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_edit.html')

    def test_product_delete_view(self):
        product = Product.objects.create(name='Test Product', quantity=10)
        response = self.client.get(reverse('product_delete', args=[product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/delete_product.html')

    def test_product_reorder_level_list_view(self):
        response = self.client.get(reverse('product_reorder_level_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_reorder_level_list.html')

    def test_export_productList_to_csv_view(self):
        response = self.client.get(reverse('export_productList_to_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'text/csv')

    def test_product_name_view(self):
        response = self.client.get(reverse('product_name'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_name.html')

    def test_product_name_list_view(self):
        response = self.client.get(reverse('product_name_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_name_list.html')

    def test_product_name_edit_view(self):
        product_name = ProductName.objects.create(name='Test Product Name')
        response = self.client.get(reverse('product_name_edit', args=[product_name.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_name_edit.html')

    def test_product_name_delete_view(self):
        product_name = ProductName.objects.create(name='Test Product Name')
        response = self.client.get(reverse('product_name_delete', args=[product_name.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_name_delete.html')

    def test_add_category_view(self):
        response = self.client.get(reverse('add_category'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_add.html')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_list.html')

    def test_category_edit_view(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.get(reverse('category_edit', args=[category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_edit.html')

    def test_category_delete_view(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.get(reverse('category_delete', args=[category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/delete_category.html')

    def test_add_department_view(self):
        response = self.client.get(reverse('add_department'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_add.html')

    def test_department_list_view(self):
        response = self.client.get(reverse('department_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_list.html')

    def test_department_edit_view(self):
        department = Department.objects.create(name='Test Department')
        response = self.client.get(reverse('department_edit', args=[department.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_edit.html')

    def test_department_delete_view(self):
        department = Department.objects.create(name='Test Department')
        response = self.client.get(reverse('department_delete', args=[department.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/delete_department.html')

    def test_add_issuance_view(self):
        response = self.client.get(reverse('add_issuance'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issuance/issuance_add.html')

    def test_issuance_list_view(self):
        response = self.client.get(reverse('issuance_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issuance/issuance_list.html')

    def test_issuance_edit_view(self):
        issuance = Issuance.objects.create(product=Product.objects.create(name='Test Product', quantity=10), quantity_issued=5, user=self.user, department=Department.objects.create(name='Test Department'))
        response = self.client.get(reverse('issuance_edit', args=[issuance.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issuance/issuance_edit.html')

    def test_issuance_delete_view(self):
        issuance = Issuance.objects.create(product=Product.objects.create(name='Test Product', quantity=10), quantity_issued=5, user=self.user, department=Department.objects.create(name='Test Department'))
        response = self.client.get(reverse('issuance_delete', args=[issuance.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issuance/delete_issuance.html')

    # Add more tests for other views...
