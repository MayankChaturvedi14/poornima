from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ContactUs(models.Model):
    user_name = models.CharField(max_length=100)
    email_id =  models.EmailField()
    phone_number = PhoneNumberField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)


class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    reg_id =  models.CharField(max_length=100)
    review = models.TextField()