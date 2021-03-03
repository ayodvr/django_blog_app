from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=204,unique=True)

# Create your models here.
class Contact(models.Model):
    fullname    = models.CharField(max_length=128)
    email       = models.EmailField(max_length=128,unique=True)
    message     = models.CharField(max_length=264)

class BoldLinks(models.Model):
    StudentName      = models.CharField(max_length=128)
    StudentEmail     = models.EmailField(max_length=128,unique=True)
    Phonenumber      = models.CharField(max_length=128)
    Address          = models.CharField(max_length=200)
    State            = models.CharField(max_length=100)
    Course           = models.CharField(max_length=128)
    Date_Enrolled    = models.CharField(max_length=100)
    Graduation_Date  = models.CharField(max_length=100)
    
    