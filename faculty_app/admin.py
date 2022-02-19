from django.contrib import admin
from .models import ContactUs
from .models import Feedback
# Register your models here.
@admin.register(ContactUs)
class SudoContact(admin.ModelAdmin):
    list_display = ['id','user_name','email_id','phone_number','state','city','course','specialization']

@admin.register(Feedback)
class SudoFeedback(admin.ModelAdmin):
    list_display = ['id','user_name','reg_id','review']