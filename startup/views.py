from django.shortcuts import render , redirect
from .models import courses , Year_1 , Year_2 , Year_3
from django.core.mail import send_mail
from django.contrib.auth.models import User,auth
from django.contrib import messages
# from django.http import HttpResponse
# Create your views here.

# context = {'baseUrl': settings.STATIC_URL}
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")


    freecourses = courses.objects.all()
    Year1 = Year_1.objects.all()
    Year2 = Year_2.objects.all()
    Year3 = Year_3.objects.all()



    if request.user.is_authenticated:
        show_contact_button = True
    else:
        show_contact_button = False
        # return render(request, 'index.html', {'show_contact_button': show_contact_button})

    return render(request, 'index.html',{'freecourses': freecourses , 'Year1' :Year1 , 'Year2' : Year2 , 'Year3': Year3,  'show_contact_button': show_contact_button})

from django.core.mail import send_mail
from django.shortcuts import render, redirect

# year 1
def sem1_view(request):
    return render(request, 'sem1_Y1.html')
def sem2_view(request):
    return render(request, 'sem2_Y1.html')

# year 2
def sem3_view(request):
    return render(request, 'sem3_Y2.html')
def sem4_view(request):
    return render(request, 'sem4_Y2.html')

# year 3
def sem5_view(request):
    return render(request, 'sem5_Y3.html')
def sem6_view(request):
    return render(request, 'sem6_Y3.html')

# core_sem1
def sem1core_view(request):
    return render(request, "core/sem1/sem1core.html")
def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nPhone:{phone}\nMessage: {message}',
            'parth02122004@gmail.com',  # replace with your email
            ['parth02122004@gmail.com'],  # replace with your email
            fail_silently=False,
        )
        return redirect('index')
    else:
        return render(request, 'index.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken (Please Choose Some Other Username )')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
                # print('email taken')
            else:
                user = User.objects.create_user(username=username, password=password1 , email=email , first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return(redirect('login'))
        else:
            messages.info(request,'password not matching...Try Again')
            return redirect('register')
    
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

