from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"faculty_main.html")

def place(request):
    return render(request,"placement.html")

def current_faculty(request):
    return render(request,'faculty.html')

def facultyLogin(request):
    return render(request,"faculty_login.html")

def faculty_profile(request):
    return render(request,"faculty_profile.html")

def current_student(request):
    return render(request,"Current_Students.html")

def about(request):
    return render(request,"About.html")

def review(request):
    return render(request,"Review.html")

def download_forms(request):
    return render(request,"downloadforms.html")

def admission(request):
    return render(request,"Admission.html")