from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

#homepage
def home(request):
    return render(request, "core/homepage.html")

#aboutus page
def aboutus(request):
    return render(request, "core/aboutuspage.html")

#mental health library page
def mhl(request):
    return render(request, "core/mhlpage.html")

#Authentication
def signupuser(request):
    if request.method == 'GET':   
        return render(request, 'core/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'core/signupuser.html',{'form':UserCreationForm(),'error':'That username has already been taken. Enter New Username'})
        else:
            return render(request, 'core/signupuser.html',{'form':UserCreationForm(),'error':'Passwords Did Not Match'})
        
def loginuser(request):
    if request.method == 'GET':   
        return render(request, 'core/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'core/loginuser.html',{'form':AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request,user)
            return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')