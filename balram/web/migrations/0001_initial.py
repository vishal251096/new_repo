# Generated by Django 2.2.1 on 2020-11-06 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400)),
                ('image', models.ImageField(upload_to='images')),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=400)),
                ('details', models.CharField(blank=True, max_length=500)),
                ('overview', models.TextField(blank=True)),
                ('created_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('actual_price', models.CharField(blank=True, max_length=10)),
                ('real_price', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
