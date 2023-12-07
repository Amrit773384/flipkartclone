from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductDetails(models.Model):
        product_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
        product_name = models.CharField(max_length=50,null=False,blank=False)
        title = models.TextField(max_length=200,default="This product is verified by the flipkart organization. Feel free to buy this one. This is default title.")
        product_prophile = models.ImageField(upload_to = 'static/productprophile images/')
        brand = models.CharField(max_length=50,null=False,blank=False)
        price = models.CharField(max_length=50)
        date = models.DateField(auto_now=True)
        stars = models.CharField(max_length=1,default='3')
        units = models.IntegerField()
        class Meta:
            verbose_name_plural = 'Products'


class ReviewDetails(models.Model):
    review = models.CharField(max_length=1000)
    product_id = models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Product Reviews"