from django.test import TestCase
from django.core.validators import MaxValueValidator
from django.utils import timezone
from ..models import Category, ProductName, Product, CustomUser, Department, Issuance

class ModelsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Category 1')
        self.product_name = ProductName.objects.create(name='Product 1')
        self.user = CustomUser.objects.create(username='user1', position='Manager', phone_number='123456789')
        self.department = Department.objects.create(name='Department 1')
        self.product = Product.objects.create(name=self.product_name, serial_no='123', quantity=10,
                                              category=self.category, reorder_level=5, release_date=timezone.now())
        self.issuance = Issuance.objects.create(quantity_issued=5, product=self.product, user=self.user,
                                                department=self.department)
    
    def test_category_str(self):
        self.assertEqual(str(self.category), 'Category 1')
    
    def test_product_name_str(self):
        self.assertEqual(str(self.product_name), 'Product 1')
    
    def test_product_str(self):
        self.assertEqual(str(self.product), 'Product 1 10')
    
    def test_custom_user_str(self):
        self.assertEqual(str(self.user), 'user1 Manager')
    
    def test_department_str(self):
        self.assertEqual(str(self.department), 'Department 1')
    
    def test_issuance_str(self):
        self.assertEqual(str(self.issuance), 'Product 1 5 Department 1 user1 %s' % self.issuance.date_issued)
    
    def test_product_quantity_validator(self):
        # Test the MaxValueValidator for product quantity
        validator = next(v for v in Product._meta.get_field('quantity').validators if isinstance(v, MaxValueValidator))
        self.assertEqual(validator.limit_value, 999999999)
    
    def test_product_reorder_level_validator(self):
        # Test the MaxValueValidator for product reorder level
        validator = next(v for v in Product._meta.get_field('reorder_level').validators if isinstance(v, MaxValueValidator))
        self.assertEqual(validator.limit_value, 9999999)
