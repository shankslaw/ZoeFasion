from django.db import models

# Create your models here.
# brand as brnd
class ProductBrand(models.Model):
    brnd_name = models.CharField(max_length=20)
    brnd_year = models.IntegerField()
    brnd_description = models.TextField()

    def __str__(self):
        return (self.brnd_name)

# product as pdt
class product(models.Model):
    pdt_name = models.CharField(max_length=100)
    pdt_image = models.ImageField(upload_to='Images')
    pdt_price = models.IntegerField()
    pdt_brand = models.ForeignKey(ProductBrand,related_name = "brand" ,on_delete=models.SET_NULL, null = True)
    pdt_description = models.TextField()

    def __str__(self):
        return (self.pdt_name)