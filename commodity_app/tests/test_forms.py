from django.test import TestCase
from django.core.exceptions import ValidationError
from ..forms import ProductForm, ProductNameForm, CategoryForm, IssuanceForm, DepartmentForm, ReorderForm
from ..models import *

class FormsTestCase(TestCase):
    def test_product_form_edit_mode(self):
        product = Product.objects.create(name=ProductName.objects.create(name='Product 1'), quantity=10)
        form = ProductForm(instance=product, edit_mode=True)
        
        for field_name in form.fields:
            self.assertTrue(form.fields[field_name].widget.attrs.get('readonly'))
    
    def test_issuance_form_edit_mode(self):
        issuance = Issuance.objects.create(quantity_issued=5, product=Product.objects.create(name=ProductName.objects.create(name='Product 1'), quantity=10))
        form = IssuanceForm(instance=issuance, edit_mode=True)
        
        for field_name in form.fields:
            self.assertTrue(form.fields[field_name].widget.attrs.get('readonly'))
    
    def test_reorder_form_readonly_name_field(self):
        product = Product.objects.create(name=ProductName.objects.create(name='Product 1'), reorder_level=5)
        form = ReorderForm(instance=product)
        
        self.assertTrue(form.fields['name'].widget.attrs.get('readonly'))
    
    def test_product_form_clean(self):
        form = ProductForm(data={'name': 'Product 1', 'quantity': -5})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)
    
    def test_category_form(self):
        form = CategoryForm(data={'name': 'Category 1'})
        self.assertTrue(form.is_valid())
        category = form.save()
        
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, 'Category 1')
    
    def test_department_form(self):
        form = DepartmentForm(data={'name': 'Department 1'})
        self.assertTrue(form.is_valid())
        department = form.save()
        
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(Department.objects.first().name, 'Department 1')
    
    def test_product_name_form(self):
        form = ProductNameForm(data={'name': 'Product 1'})
        self.assertTrue(form.is_valid())
        product_name = form.save()
        
        self.assertEqual(ProductName.objects.count(), 1)
        self.assertEqual(ProductName.objects.first().name, 'Product 1')
    
    def test_issuance_form(self):
        product = Product.objects.create(name=ProductName.objects.create(name='Product 1'), quantity=10)
        user = CustomUser.objects.create(username='user1', position='Manager', phone_number='123456789')
        department = Department.objects.create(name='Department 1')
        form = IssuanceForm(data={'quantity_issued': 5, 'product': product.id, 'user': user.id, 'department': department.id})
        self.assertTrue(form.is_valid())
        issuance = form.save()
        
        self.assertEqual(Issuance.objects.count(), 1)
        self.assertEqual(Issuance.objects.first().product, product)
        self.assertEqual(Issuance.objects.first().quantity_issued, 5)
        self.assertEqual(Issuance.objects.first().user, user)
        self.assertEqual(Issuance.objects.first().department, department)
