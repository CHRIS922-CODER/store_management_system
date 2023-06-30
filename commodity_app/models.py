from django.db import models
from django.core.validators import  MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import User,AbstractUser,AnonymousUser
from django.contrib.auth import get_user_model
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
         return f"{self.name}"

class ProductName(models.Model):
     name = models.CharField(max_length=50)
     def __str__(self):
          return f"{self.name}"
     
     def save(self,*args, **kwargs):
         self.name = self.name.capitalize()
         super().save(*args,**kwargs)

class Product(models.Model):
    name =  models.ForeignKey(ProductName,on_delete=models.CASCADE)
    serial_no = models.CharField(max_length=50, null=True, default=0)
    quantity = models.PositiveBigIntegerField(validators=[MaxValueValidator(999999999)]) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    reorder_level = models.PositiveIntegerField(validators=[MaxValueValidator(9999999)],default=0)
    release_date = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.name} {str(self.quantity)}"
    
    def save(self,*args, **kwargs):
         self.name = self.name
         super().save(*args,**kwargs)
         

class CustomUser(AbstractUser):
     position = models.CharField(max_length=100)
     phone_number = models.CharField(max_length=20)

     def __str__(self):
          return f"{self.username} {self.position}"
     
     class Meta:
          swappable = 'AUTH_USER_MODEL'
          default_related_name = 'custom_users'
          
class Department(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
           return f"{self.name}"
      
class Issuance(models.Model):
    quantity_issued = models.PositiveBigIntegerField(validators=[MaxValueValidator(999999999)])
    date_issued = models.DateTimeField(default=timezone.now().strftime('%Y-%m-%d %H:%M:%S'))
    status = models.BooleanField(default=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} {self.quantity_issued} {self.department} {self.user} {self.date_issued}"

      



