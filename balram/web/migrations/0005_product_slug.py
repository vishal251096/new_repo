# Generated by Django 2.2.1 on 2020-11-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_combo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
