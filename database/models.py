from django.db import models


class Testimonial(models.Model):
    address = models.CharField(max_length=100)
    rating = models.FloatField()
    img = models.ImageField(upload_to='Picture') 
    name = models.CharField(max_length=20)
    occupation = models.CharField(max_length=100)
    opinion = models.TextField()
    
class About(models.Model):
    birthday = models.DateField()
    website=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    city=models.CharField(max_length=100)
    
class Aboutextra(models.Model): 
    age=models.IntegerField()  
    degree=models.CharField(max_length=150)
    email=models.EmailField(max_length=250,unique=True)
    freelancer=models.CharField(max_length=150)
    

class Hero(models.Model): 
    heroimg=models.ImageField(upload_to='Picture')
    heroname=models.CharField(max_length=200)    
    favicon=models.ImageField(upload_to='Picture')
    favapple=models.ImageField(upload_to='Picture')
    
class HeroCV(models.Model): 
    file = models.FileField(upload_to='Picture',null=True, blank=True)
    
    
    
    
      # #about area
    # aboutlist = [
    # {'label': 'Birthday:', 'value': '03/06/2005'},
    # {'label': 'Website:', 'value': 'monjurulislamshoron.com'},
    # {'label': 'Phone:', 'value': '+8801771-224762'},
    # {'label': 'City:', 'value': 'Dhaka-Bangladesh'},]
    
    # about_list=[
    # {'label1': 'Age:', 'value1': '20'},
    # {'label1': 'Degree:', 'value1': 'Diploma'},
    # {'label1': 'Email:', 'value1': 'monjurulislamshoron2005@gmail.com'},
    # {'label1': 'Freelance:', 'value1': 'Available'},]   

# Create your models here.
