from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login as login_f, authenticate, logout as logout_f
from django.contrib.auth.forms import AuthenticationForm

# endpoint to render index page for all users
def index(request):
    if request.method == 'GET':
        return render(
            request,
            'Main/index.html'
        )

# renders registration page for all users
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login_f(request, user)
            messages.success(request, "Registration successful." )
            return redirect("Main:index")
        else:
            messages.error(request, "Unsuccessful registration.")
    else:
        form = RegistrationForm()
    return render(request, 'Main/register.html', {'form': form})

#  renders login page for all users
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_f(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Main:index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "Main/login.html", context={"form": form})

def logout(request):
	logout_f(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("Main:index")