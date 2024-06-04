from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required (login_url='login')
def homePage(request):
    return render(request, 'home.html')

def loginPage(request):
    if request.method == "POST":
        uname = request.POST['username']
        pass1 = request.POST['pass1']
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           return HttpResponse("<h1>Invalid Login</h1>")
    return render(request, 'login.html')

def  signupPage(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if username and email and password and confirm_password is not None:
            if password!=confirm_password:
                return HttpResponse("<h1>Passwords do not match.</h1>")
            else:
                my_user=User.objects.create_user(username,email,password)
                my_user.save()
                return redirect('login')
        else:
            return HttpResponse("<h1>Please fill all fields.</h1>")
    return render(request, 'signup.html')

def logoutPage(request):
    logout(request)
    return redirect('login')