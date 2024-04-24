from django.db import models
from books_brand.models import BrandModels
# Create your models here.
class PostModel(models.Model):
    brand = models.ForeignKey(BrandModels,related_name='brand',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    borrowed_price = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    image = models.ImageField(upload_to='post/media/upload',blank=True,null=True)

    
