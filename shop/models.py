from django.db import models

# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.title
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description= models.TextField()
    image = models.CharField(max_length=300)


class Orders(models.Model):
    def __str__(self):
        return self.name
    item = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    total=models.CharField(max_length=2000)
    

