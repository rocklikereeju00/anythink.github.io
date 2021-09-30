from django.db import models


# Create your models here.
class Item(models.Model):
        name=models.CharField(max_length=122)
        email=models.CharField(max_length=122)
        phone=models.CharField(max_length=12)
        address=models.TextField()
        address2=models.TextField()
        City_Village=models.CharField(max_length=122)
        dic=models.CharField(max_length=122)
        atta=models.TextField()
        zip=models.CharField(max_length=122)
        date=models.DateField()


        def __str__(self) :
            return self.name