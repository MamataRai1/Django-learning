from django.db import models

class person(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media',null=True,blank=True)
