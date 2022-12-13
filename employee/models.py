from django.db import models
import uuid
from django.contrib.auth.models import User

class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    emp_name = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()
    
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.emp_name

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        
        return url


class Address(models.Model):
    address = models.TextField()
    employee = models.ForeignKey('Employee',on_delete=models.SET_NULL, null=True, blank=True, related_name='addresses')