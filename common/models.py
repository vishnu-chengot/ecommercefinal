from django.db import models

# Create your models here.

class Customer(models.Model):
   first_name = models.CharField(max_length=20)
   second_name = models.CharField(max_length=20)
   email = models.CharField(max_length=50)
   password =models.CharField(max_length=20)
   phone = models.BigIntegerField()
   address = models.TextField()
   
   class Meta:
      db_table = 'customer_tb'

class seller(models.Model):
   first_name = models.CharField(max_length=50)
   second_name = models.CharField(max_length=50)
   email = models.CharField(max_length=30)
   password = models.CharField(max_length=20)
   user_name = models.IntegerField(default=0)
   phone = models.BigIntegerField()
   address = models.TextField()
   bank_name = models.CharField(max_length=20)
   account_number = models.BigIntegerField()
   ifsc = models.CharField(max_length=10)
   seller_pic = models.ImageField(upload_to='seller/')

   class Meta:
      db_table = 'seller_tb'