from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    FirstName = models.CharField(max_length=50, verbose_name='First Name')
    LastName = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.CharField(max_length=100)
    mobile_no_validator = RegexValidator(regex=r'\d{10}', message="Phone number must be 10 digits only!!")
    mobile = models.CharField(validators=[mobile_no_validator], max_length=10)

    def __str__(self):
        return f'User: [{self.FirstName} {self.LastName}] with Username: [{self.username}]'


class Speaker(User):
    EmergencyContactName = models.CharField(max_length=100, verbose_name='Emergency Contact')
    EmergencyContactNumber = models.CharField(validators=[User.mobile_no_validator], max_length=10, verbose_name='Emergency Contact Number')
    GitHub = models.CharField(max_length=200)
    Twitter = models.CharField(max_length=200, blank=True)
    LinkedIn = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Speaker: [{self.FirstName} {self.LastName}] with Username: [{self.username}]'


class Venue(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    description = models.TextField()
    address = models.TextField(unique=True)
    website = models.CharField(max_length=300, unique=True)
    contact = models.CharField(max_length=100)
    verified = models.BooleanField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return f'Venue: [{self.name}] with website: [{self.website}]'


class RegisteredUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
