# Generated by Django 4.0.6 on 2022-09-05 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sams', '0004_alter_category_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
