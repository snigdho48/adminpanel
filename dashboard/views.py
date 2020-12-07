from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name= request.POST['First_Name']
        last_name= request.POST['Last_Name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken.')

                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken.')

                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'Account created successfully.')
                return redirect('register')

        else:
            messages.info(request,"Password didn't match.")
            return redirect('register')

    else:
            return render(request,'register.html')


def login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('username')
        password= request.POST.get('password')
        User._meta.get_field('email')._unique = True



        if User.objects.filter(username=username).exists():
            user= auth.authenticate(username=username,password=password)



        elif User.objects.filter(email=email).exists():
            username = User.objects.get(email=email.lower()).username
            user= authenticate(username=username,password=password)



        else:
            messages.info(request,'Enter valid username or email')
            return redirect('login')





        if user is not None:

            auth.login(request,user)
            messages.info(request,'Signin successfully.')
            return redirect('/',)

        else:
            messages.info(request,'incorrect password.')
            return redirect('login')



    else:
        return render(request,'login.html')






def logout(request):

    auth.logout(request)
    return redirect('login')


def layout(request):
    return render(request,'layout-light.html')

def base(request):
    return render(request,'base.html')

def password(request):
    return render(request,'password.html')

def tables(request):
    return render(request,'tables.html')

def charts(request):
    return render(request,'charts.html')

def cards(request):
    return render(request,'cards.html')

def e500(request):
    return render(request,'500.html')

def e401(request):
    return render(request,'401.html')

def e404(request):
    return render(request,'404.html')

def index(request):
    return render(request,'index.html')
