from django.db import models

class User_data(models.Model):
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_city = models.CharField(max_length=100)
    user_hobby = models.CharField(max_length=100)
    user_food = models.CharField(max_length=100)  

    def __str__(self):
        return str(self.user_name)



from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_description = models.TextField()
    product_photo = models.ImageField(upload_to="products/")
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Products"   
        ordering = ["product_name"]    
    def __str__(self):
        return f"{self.product_name} - {self.product_price}"

