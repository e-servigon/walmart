# Generated by Django 4.0.6 on 2022-09-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sams', '0011_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_sku',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
