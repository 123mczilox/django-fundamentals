from django.db import models

class ChildrenHome(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="used for the URLs")
    COUNTY_CHOICES = [
        ('Nairobi', 'Nairobi'),('Nyandarua','Nyandarua'),('Nyeri','Nyeri'),('Kirinyaga','Kirinyaga'),
        ('Kiambu','Kiambu'),('Mombasa', 'Mombasa'),
    ]
    location = models.CharField(max_length=100, choices=COUNTY_CHOICES)
    capacity = models.IntegerField()
    descripttion = models.TextField()
    image = models.ImageField(upload_to='children_homes/')
    website_url = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField() 
    is_verified = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False, help_text="Check this to show on 'Urgent Needs' section")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    height = models.FloatField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name