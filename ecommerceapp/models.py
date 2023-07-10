from django.db import models

class products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description= models.TextField()
    image = models.CharField(max_length=200)

class order(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.CharField( max_length=200)
    dire= models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code= models.CharField(max_length=200)
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
