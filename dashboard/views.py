from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def layout(request):
    return render(request,'layout-light.html')

def base(request):
    return render(request,'base.html')

def login(request):
    return render(request,'login.html')

def password(request):
    return render(request,'password.html')

def register(request):
    return render(request,'register.html')

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
