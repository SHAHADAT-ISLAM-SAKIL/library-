from django.db import models

# Create your models here.
class BrandModels(models.Model):
    brand_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True,null=True,blank=True)
    def __str__(self) -> str:
        return self.brand_name