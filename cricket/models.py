from django.db import models

# Create your models here.

class player(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)

class filedata(models.Model):
    myfile=models.FileField(upload_to='documents/%Y/%m/%d')



class filedatacheck(models.Model):
    myfile=models.FileField(upload_to='documents/%Y/%m/%d')
    sha1 = models.CharField(max_length=400)
    sha256 = models.CharField(max_length=400)
    md5=models.CharField(max_length=400)

class userprofile(models.Model):
    name=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class sha256hash(models.Model):
    value=models.CharField(max_length=400)

class sha1hash(models.Model):
    value=models.CharField(max_length=400)

class md5hash(models.Model):
    value=models.CharField(max_length=400)

class dataset(models.Model):
    myfile=models.FileField(upload_to='documents/%Y/%m/%d')

class validfiles(models.Model):
    myfile=models.FileField(upload_to='documents/%Y/%m/%d')







