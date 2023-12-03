from django.shortcuts import render
from .forms import RegisterForm
from .models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def register(request):
    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save() 
            return redirect('login')
    else:
        user=RegisterForm()
        
    return render(request,'user_auth/register.html',{'rf':user})
            
    

def get_login(request):
    if request.method == 'POST':
        user_email   = request.POST.get('email')
        user_password= request.POST.get('password')
        user = authenticate(request,email=user_email,password = user_password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'user_auth/login.html',{"error":"Wrong Password or Email"})
      
             
    return render(request,'user_auth/login.html')



def logout_user(request):
    logout(request)
    return redirect('login')