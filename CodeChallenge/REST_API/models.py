from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserOrganization(models.Model):
    users = models.ForeignKey('User', on_delete=models.CASCADE)
    organizations = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.users

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique = True)
    address = models.TextField(max_length=40)
    phone = models.BigIntegerField(null=True)
    organizations = models.ManyToManyField('Organization', through=UserOrganization, blank=True)

    class Meta:
        ordering = ['email']


    def __str__(self):
        return self.email

class Organization(models.Model):
    users = models.ManyToManyField('User', through=UserOrganization, blank=True)
    name = models.CharField(max_length=40, unique=True, primary_key=True)
    address = models.TextField(max_length=40)
    phone = models.BigIntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
