from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    height = models.FloatField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
class hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    requiremets = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
