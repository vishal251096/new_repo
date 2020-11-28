from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=400, blank=True)
    image = models.ImageField(upload_to='images')
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    description = models.CharField(max_length=400, blank=True)
    details = models.CharField(max_length=500, blank=True)
    overview = models.TextField(blank=True)
    created_date = models.DateField(default=timezone.now, blank=True)
    category = models.CharField(max_length=100, blank=True)
    actual_price = models.CharField(max_length= 10, blank=True)
    real_price = models.CharField(max_length= 10, blank=True)
    slug = models.SlugField(null=False, unique=True)


    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.name


class Combo(models.Model):
    name = models.CharField(max_length=400, blank=True)
    details = models.CharField(max_length=500, blank=True)
    overview = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    item1_image = models.ImageField(upload_to='images', blank=True)
    item2_image = models.ImageField(upload_to='images', blank=True)
    item3_image = models.ImageField(upload_to='images', blank=True)
    item4_image = models.ImageField(upload_to='images', blank=True)
    item5_image = models.ImageField(upload_to='images', blank=True)
    created_date = models.DateField(default=timezone.now, blank=True)
    price = models.CharField(max_length= 10, blank=True)
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse('combo_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
