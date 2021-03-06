# Generated by Django 2.2.1 on 2020-11-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201107_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='combo',
            name='item1_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='item2_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='item3_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='item4_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='item5_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
