from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_date = models.DateTimeField()

    def __str__ (self):
        return 'la categoria es: %s' % (self.category_name)

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_category = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    def __str__ (self):
        return 'el proveedor es: %s %s' % (self.vendor_name,self.vendor_category )

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_size = models.CharField(max_length=255)
    product_color = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255)
    created_date = models.DateTimeField()

    def __str__ (self):
        return 'el producto es: %s %s %s' % (self.product_name, self.product_size, self.product_color)