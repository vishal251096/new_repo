# Generated by Django 2.2.1 on 2020-11-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
