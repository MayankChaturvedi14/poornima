"""faculty_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from faculty_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="faculty-view-page"),
    path('p',views.place, name="placement"),
    path('f',views.facultyLogin, name="faculty_login"),
    path('cf',views.current_faculty, name="current_faculty"),
    path('fp',views.faculty_profile, name="faculty_profile"),
    path('cs',views.current_student, name="current_student"),
    path('abt',views.about, name="about"),
    path('revu',views.review,name="review"),
    path('df',views.download_forms,name="download_forms"),
    path('ad',views.admission,name="admission"),
]
