from django.db import models
from common.models import seller

# Create your models here.


class Product(models.Model):
   seller = models.ForeignKey(seller,on_delete=models.CASCADE)
   product_name = models.CharField(max_length=20)
   category_name = models.CharField(max_length=20)
   product_number = models.BigIntegerField()
   product_discription =models.CharField(max_length=60)
   price = models.IntegerField()
   stock = models.IntegerField()
   image = models.ImageField(upload_to='product/')
   
   class Meta:
      db_table = 'product_tb'