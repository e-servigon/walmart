# Generated by Django 4.0.6 on 2022-09-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sams', '0005_alter_category_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_sku',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
