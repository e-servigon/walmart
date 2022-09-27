from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ExtendedData(models.Model):
    TYPE_CHOICES = [("B","Comprador"), ("R","Replenisher")]
    user_type = models.CharField(max_length=1, choices= TYPE_CHOICES)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    def __str__ (self):
        return 'el user_type es: %s' % (self.user_type)  

class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__ (self):
        return 'la categoria es: %s' % (self.category_name)

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    vendor_category = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(default = timezone.now, blank=True, null=True)
  
    def __str__ (self):
         return '%s' % (self.vendor_name)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_size = models.CharField(max_length=255,blank=True, null=True)
    product_color = models.CharField(max_length=255,blank=True, null=True)
    product_sku = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default= timezone.now, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def __str__ (self):
        return 'el producto es: %s %s %s' % (self.product_name, self.product_size, self.product_color)