from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField('published')
    modified_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    registration_time = models.DateTimeField(auto_now=False, auto_now_add=True)
