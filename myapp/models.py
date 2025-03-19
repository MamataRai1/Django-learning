from django.db import models

class person(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)


# class students(models.Model):
#     name=models.CharField(max_length=100)
#     age=models.IntegerField()
#     address=models.CharField(max_length=50)
#     description=models.TextField(null=True)