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

class Career(models.Model):
    #Personal Details
    user_name = models.CharField(max_length=100)
    email_id =  models.EmailField()
    birth_place = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    #Professionals Details
    applied_for = models.CharField(max_length=50)
    designation =  models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    UG = models.CharField(max_length=10)
    PG = models.CharField(max_length=10)
    DOC = models.CharField(max_length=10)
    Teaching_since = models.CharField(max_length=10)
    Corporate_experience = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    #Academic Details

    #UG
    ugpassing_year = models.CharField(max_length=5,null = True)
    ugpercentage = models.CharField(max_length=5,null = True)
    ugcollege = models.CharField(max_length=50)
    uguniversity = models.CharField(max_length=50)
    ugcity = models.CharField(max_length=50)
    ugbranch = models.CharField(max_length=10)

    #PG
    pgpassing_year = models.CharField(max_length=5,null = True)
    pgpercentage = models.CharField(max_length=5,null = True)
    pgcollege = models.CharField(max_length=50, null = True)
    pguniversity = models.CharField(max_length=50, null = True)
    pgcity = models.CharField(max_length=50, null = True)
    pgareaofexp = models.CharField(max_length=50, null = True)
    pgthesis_title = models.CharField(max_length=50, null = True)

    #PHD
    docpassing_year = models.CharField(max_length=5,null = True)
    docstatus = models.CharField(max_length=10, null = True,default="NA")
    doccollege = models.CharField(max_length=50, null = True)
    docuniversity = models.CharField(max_length=50, null = True)
    doccity = models.CharField(max_length=50, null = True)
    docareaofexp = models.CharField(max_length=50, null = True)
    docthesis_title = models.CharField(max_length=50, null = True)

    #Resume
    resume = models.FileField(upload_to='documents/%Y/%m/%d')
