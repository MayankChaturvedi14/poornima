from atexit import register
from django.http import request
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactUs,Feedback
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"demo.html")

def place(request):
    return render(request,"placement.html")

def current_faculty(request):
    return render(request,'faculty.html')

def facultyLogin(request):
    return render(request,"faculty_login.html")

def faculty_view(request):
    return render(request,"faculty_main.html")

def faculty_profile(request):
    return render(request,"faculty_profile.html")

def current_student(request):
    return render(request,"Current_Students.html")

def about(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        state = request.POST["stt"]
        city = request.POST["city"]
        course = request.POST["course"]
        specialization = request.POST["spec"]
        # return HttpResponse(f"name = {name} email={email} state={state} course={course}")
        record = ContactUs(user_name=name,email_id=email,phone_number=phone,state=state,city=city,course=course,specialization=specialization)
        record.save()
        messages.info(request, 'Record saved successfully!')
        return redirect(about)
    return render(request,"About.html")

def review(request):
    peak=""
    if request.method=="POST":
        name = request.POST["name"]
        reg_no = request.POST["reg_no"]
        Review = request.POST["review"]
        record = Feedback(user_name=name,reg_id=reg_no,review=Review)
        record.save()
        messages.info(request, 'Record saved successfully!')
        peak = Feedback.objects.all()
        return redirect(review,{'views':peak})
    peak = Feedback.objects.all()
    return render(request,"Review.html",{'views':peak})

def download_forms(request):
    return render(request,"downloadforms.html")

def admission(request):
    return render(request,"Admission.html")

def career(request):
    return render(request,"Career.html")

def hostal(request):
    return render(request,"hostal.html")