from django.shortcuts import render,redirect
from .models import ContactUs,Feedback,Career,FacultyProfile
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.
def home(request):
    return render(request,"demo.html")

def place(request):
    return render(request,"placement.html")

def current_faculty(request):
    return render(request,'Faculty.html')


def faculty_view(request):
    return render(request,"faculty_main.html")

@login_required(login_url='/f/')
def faculty_profile(request):
    user_email = request.user.email
    if request.method=="POST":
        edu = request.POST["edu"]
        aoi = request.POST["aoi"]
        sub = request.POST["sub"]
        publications = request.POST["publications"]
        research_papers = request.POST["research_papers"]
        record = FacultyProfile.objects.get(email=user_email)
        if not edu==record.education:
            record.education = edu
        if not aoi==record.areaofinterest:
            record.areaofinterest = aoi
        if not sub==record.subjects:
            record.subjects=sub
        if not publications==record.publications:
            record.publications = publications
        if not research_papers==record.research:
            record.research=research_papers
        record.save()
    try:
        at = FacultyProfile.objects.get(email=user_email)
        print("\n\n\n=======>",at.publications,"\n\n\n")
        return render(request,"Faculty_profile.html",{"user_details":request.user,"profile_details":at})
    except:
        return render(request,"Faculty_profile.html",{"user_details":request.user,"profile_details":"Non available","media_url":settings.MEDIA_URL})
   

@login_required(login_url='/f/')
def logout(request):
    django_logout(request)
    return redirect(current_faculty)

def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None

def facultyLogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            f_email = request.POST["Email"]
            f_password = request.POST["Password"]
            user = authenticate_user(f_email, f_password)
            if user is not None:
                login(request,user)
                if request.GET.get('next', None):
                    return redirect(request.GET['next']) 
                return redirect(faculty_profile)
        return render(request,"faculty_login.html")
    return redirect(faculty_profile)

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
        return render(request,"review.html",{'views':peak})
    peak = Feedback.objects.all()  
    messages.info(request, None)
    return render(request,"review.html",{'views':peak})

def download_forms(request):
    return render(request,"downloadforms.html")

def admission(request):
    return render(request,"Admission.html")

def career(request):
    if request.method=="POST":
        #Personal details
        name = request.POST["name"]
        email = request.POST["email"]
        place = request.POST["place"]
        phone = request.POST["phone"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]

        #professional details
        postappliedfor = request.POST["postappliedfor"]
        designation = request.POST["designation"]
        department = request.POST["Department"]
        UG = request.POST["U.G"]
        PG = request.POST["P.G"]
        Doctorate = request.POST["Doctorate"]
        TExp = request.POST["Teaching Exp"]
        CoExp = request.POST["Corporate Exp"]
        crnt_loc = request.POST["Cloc"]

        #Academic details
        #UG
        UGPass = request.POST["UGPass"]
        UGpercent = request.POST["percent"]
        UGcollege_name = request.POST["college_name"]
        UGUniversity_name = request.POST["University_name"]
        UGcity = request.POST["city"]
        UGbranch = request.POST["branch"]

        #PG
        PGPass = request.POST["PGPass"]
        PGpercent = request.POST["PGpercent"]
        PGcollege_name = request.POST["PGcollege_name"]
        PGUniversity_name = request.POST["PGuniversity_name"]
        PGcity = request.POST["PGCity"]
        PGAExp = request.POST["PGAOExp"]
        PGThesis = request.POST["PGThesis"]

        #PHD
        PHDPass = request.POST["PHDPass"]
        PHDstate = request.POST["PHDstate"]
        PHDcollege_name = request.POST["PHDcollege_name"]
        PHDUniversity_name = request.POST["PHDUniversity_name"]
        PHDcity = request.POST["PHDcity"]
        PHDAExp = request.POST["PHDAExp"]
        PHDThesis = request.POST["PHDThesis"]
        doc_file=request.FILES.get("resume")
        print("Doc file:-",doc_file)
        if(PG=="NA" and Doctorate=="NA"):
            record = Career(user_name=name,email_id=email,birth_place=place,phone_number=phone,dob=dob,gender=gender,
            applied_for=postappliedfor,designation=designation,department=department,UG=UG,PG=PG,DOC=Doctorate,Teaching_since=TExp,Corporate_experience=CoExp,city=crnt_loc,
            ugpassing_year=UGPass,ugpercentage=UGpercent,ugcollege=UGcollege_name,uguniversity=UGUniversity_name,ugcity=UGcity,ugbranch=UGbranch,
            resume=doc_file
            )
        elif(Doctorate=="NA"):
            record = Career(user_name=name, email_id=email, birth_place=place,  phone_number=phone, dob=dob,    gender=gender,
            applied_for=postappliedfor, designation=designation,    department=department,  UG=UG,PG=PG,DOC=Doctorate,  Teaching_since=TExp,    Corporate_experience=CoExp, city=crnt_loc,
            ugpassing_year=UGPass,  ugpercentage=UGpercent,ugcollege=UGcollege_name,uguniversity=UGUniversity_name,ugcity=UGcity,ugbranch=UGbranch,
            pgpassing_year=PGPass,  pgpercentage=PGpercent, pgcollege=PGcollege_name,   pguniversity=PGUniversity_name, pgcity=PGcity,  pgareaofexp=PGAExp, pgthesis_title=PGThesis,
            resume=doc_file
            )
        else:
            record = Career(user_name=name, email_id=email, birth_place=place,  phone_number=phone, dob=dob,    gender=gender,
            applied_for=postappliedfor, designation=designation,    department=department,  UG=UG,PG=PG,DOC=Doctorate,  Teaching_since=TExp,    Corporate_experience=CoExp, city=crnt_loc,
            ugpassing_year=UGPass,  ugpercentage=UGpercent,ugcollege=UGcollege_name,uguniversity=UGUniversity_name,ugcity=UGcity,ugbranch=UGbranch,
            pgpassing_year=PGPass,  pgpercentage=PGpercent, pgcollege=PGcollege_name,   pguniversity=PGUniversity_name, pgcity=PGcity,  pgareaofexp=PGAExp, pgthesis_title=PGThesis,
            docpassing_year=PHDPass,  docstatus=PHDstate, doccollege=PHDcollege_name,   docuniversity=PHDUniversity_name, doccity=PHDcity,  docareaofexp=PHDAExp, docthesis_title=PHDThesis,
            resume=doc_file
            )
        record.save()
        messages.info(request, 'Record saved successfully!')
        return redirect(career)
    return render(request,"Career.html")

def hostal(request):
    return render(request,"hostal.html")

def technical_events(request):
    return render(request,"technical events.html")

def get_user_profile(request,username):
    user = User.objects.get(username=username)
    at = FacultyProfile.objects.get(email=user.email)
    return render(request, 'user_profile.html', {"user_details":user,"profile_details":at,"media_url":settings.MEDIA_URL})

def Gallery(request):
    return render(request,"Gallery.html")