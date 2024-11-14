from django.db import models

# Create your models here.

class courses(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    link = models.TextField()

# Year Wise
class Year_1(models.Model):
    
    name = models.CharField(max_length=400)
    tag = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='pics')
    description = models.TextField()
    # applied = models.TextField()
    # link = models.TextField(default='https://classickcode-4zfw.onrender.com')

class Year_2(models.Model):

    name = models.CharField(max_length=400)
    tag = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='pics')
    description = models.TextField()
    # applied = models.TextField()
    # link = models.TextField(default='https://classickcode-4zfw.onrender.com')

class Year_3(models.Model):

    name = models.CharField(max_length=400)
    tag = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='pics')
    description = models.TextField()
    # applied = models.TextField()
    # link = models.TextField(default='https://classickcode-4zfw.onrender.com')

# Semester wise 