from django.db import models

# Create your models here.

class courses(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    link = models.TextField()

class jobs(models.Model):
    
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    applied = models.TextField()
    link = models.TextField()

class internships(models.Model):

    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    applied = models.TextField()
    link = models.TextField()
