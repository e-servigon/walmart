# Generated by Django 4.0.6 on 2024-09-09 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sams', '0003_extendeddata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]