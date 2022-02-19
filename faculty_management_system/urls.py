
from django.contrib import admin
from django.urls import path
from faculty_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('p',views.place, name="placement"),
    path('f',views.facultyLogin, name="faculty_login"),
    path('cf',views.current_faculty, name="current_faculty"),
    path('fv',views.faculty_view, name="faculty-view"),
    path('fp',views.faculty_profile, name="faculty_profile"),
    path('cs',views.current_student, name="current_student"),
    path('abt',views.about, name="about"),
    path('revu',views.review,name="review"),
    path('df',views.download_forms,name="download_forms"),
    path('ad',views.admission,name="admission"),
    path('hostals',views.hostal,name="hostal"),
    path('career',views.career,name="career"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
