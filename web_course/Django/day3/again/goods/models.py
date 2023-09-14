from django.db import models

# Create your models here.
# class명 pascal case
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField()
    created_app = models.DateField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now=True)

# db날리기 > db.sqlite3 삭제
# makemigrations
# migrate