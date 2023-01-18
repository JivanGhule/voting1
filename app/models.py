from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=100,null=False)
    browser=models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return self.name
    
class UserRegistartion(models.Model):
    name=models.CharField(max_length=100,null=False)
    adhar_number=models.PositiveIntegerField(null=False)
    mobile_number=models.PositiveIntegerField(null=False)
    address=models.TextField(max_length=100,null=False)
    age=models.PositiveIntegerField(null=False)
    UID=models.TextField(max_length=100,null=False)
    
    def __str__(self):
        return self.name